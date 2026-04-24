import React, { useState, useEffect, useRef } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity, ScrollView, Alert, Modal, ActivityIndicator } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { CameraView, useCameraPermissions } from 'expo-camera';
import { Picker } from '@react-native-picker/picker';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { producaoService, auxService } from '../services';
import { useTheme } from '../context/ThemeContext';

export default function ApontamentoScreen() {
  const [codigoBarra, setCodigoBarra] = useState('');
  const [idSetor, setIdSetor] = useState('');
  const [idOperador, setIdOperador] = useState('');
  const { colors, dark } = useTheme();
  
  const [listaSetores, setListaSetores] = useState([]);
  const [listaOperadores, setListaOperadores] = useState([]);
  const [isFocused, setIsFocused] = useState(false);
  const inputRef = useRef(null);
  
  const [loading, setLoading] = useState(false);
  const [scanning, setScanning] = useState(false);
  const [activeTarget, setActiveTarget] = useState('pneu'); // 'pneu' ou 'operador'
  const [isFocusedOperador, setIsFocusedOperador] = useState(false);
  const inputOperadorRef = useRef(null);
  const [permission, requestPermission] = useCameraPermissions();

  useEffect(() => {
    fetchAuxiliares();
    loadDefaults();
    // Auto-focus no campo de código de barras ao abrir a tela
    setTimeout(() => {
      if (inputRef.current) {
        inputRef.current.focus();
      }
    }, 500);
  }, []);

  const fetchAuxiliares = async () => {
    try {
      const setores = await auxService.listarSetores();
      const operadores = await auxService.listarOperadores();
      setListaSetores(setores);
      setListaOperadores(operadores);
    } catch (error) {
      console.warn('Erro ao carregar dados auxiliares:', error);
    }
  };

  const loadDefaults = async () => {
    try {
      const savedSetor = await AsyncStorage.getItem('default_setor');
      const savedOperador = await AsyncStorage.getItem('default_operador');
      if (savedSetor) setIdSetor(parseInt(savedSetor));
      if (savedOperador) setIdOperador(parseInt(savedOperador));
    } catch (error) {
      console.error('Erro ao carregar padrões:', error);
    }
  };

  const handleScan = ({ data }) => {
    if (activeTarget === 'pneu') {
      setCodigoBarra(data);
    } else {
      setIdOperador(data);
    }
    setScanning(false);
  };

  const openScanner = async (target = 'pneu') => {
    setActiveTarget(target);
    if (!permission?.granted) {
      const { status } = await requestPermission();
      if (status !== 'granted') {
        Alert.alert('Permissão Negada', 'O acesso à câmera é necessário para o scanner.');
        return;
      }
    }
    setScanning(true);
  };

  const handleSalvar = async () => {
    if (!codigoBarra || !idSetor || !idOperador) {
      Alert.alert('Campos Obrigatórios', 'Escolha o Setor e o Operador.');
      return;
    }

    setLoading(true);
    try {
      const pneu = await producaoService.buscarPneu(codigoBarra);
      
      const novoApontamento = {
        codigo_barra: codigoBarra,
        id_pneu: pneu.id,
        id_setor: parseInt(idSetor),
        id_operdor: parseInt(idOperador),
        data_inicio: new Date().toISOString().split('T')[0],
      };

      await producaoService.criar(novoApontamento);
      Alert.alert('Sucesso', 'Produção iniciada com sucesso!');
      setCodigoBarra('');
    } catch (error) {
      Alert.alert('Erro', 'Pneu não localizado ou erro na gravação.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={[styles.container, { backgroundColor: colors.background }]}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={[styles.header, { color: colors.text }]}>Apontamento</Text>
        <Text style={[styles.subHeader, { color: colors.textSecondary }]}>Preencha os dados e escaneie o pneu.</Text>

        <View style={styles.formGroup}>
          <Text style={[styles.label, { color: colors.textSecondary }]}>Setor Móvel</Text>
          <View style={[styles.pickerContainer, { backgroundColor: colors.inputBackground, borderColor: colors.border }]}>
            <Picker
              selectedValue={idSetor}
              onValueChange={(val) => setIdSetor(val)}
              style={[styles.picker, { color: colors.text }]}
              dropdownIconColor={colors.text}
            >
              <Picker.Item label="Escolha o Setor..." value="" color={colors.textSecondary} />
              {listaSetores.map(s => (
                <Picker.Item key={s.ID} label={s.DESCRICAO} value={s.ID} color={colors.text} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.formGroup}>
          <Text style={[styles.label, { color: colors.textSecondary }]}>Pneu (Código de Barras)</Text>
          <View style={styles.inputWrapper}>
            <TextInput 
              ref={inputRef}
              style={[
                styles.input, 
                { backgroundColor: colors.inputBackground, borderColor: colors.border, color: colors.text },
                isFocused && { backgroundColor: dark ? '#555500' : '#FFFF00' }
              ]} 
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
              placeholder="Escaneie o Pneu..." 
              placeholderTextColor={colors.textSecondary}
              value={codigoBarra}
              onChangeText={setCodigoBarra}
            />
            <TouchableOpacity style={[styles.scannerBtn, { backgroundColor: colors.primary }]} onPress={() => openScanner('pneu')}>
              <MaterialCommunityIcons name="barcode-scan" size={24} color="#FFFFFF" />
            </TouchableOpacity>
          </View>
        </View>

        <View style={styles.formGroup}>
          <Text style={[styles.label, { color: colors.textSecondary }]}>Operador Responsável</Text>
          <View style={styles.inputWrapper}>
            <TextInput 
              ref={inputOperadorRef}
              style={[
                styles.input, 
                { backgroundColor: colors.inputBackground, borderColor: colors.border, color: colors.text },
                isFocusedOperador && { backgroundColor: dark ? '#555500' : '#FFFF00' }
              ]} 
              onFocus={() => setIsFocusedOperador(true)}
              onBlur={() => setIsFocusedOperador(false)}
              placeholder="Digite ou Escaneie o ID..." 
              placeholderTextColor={colors.textSecondary}
              value={idOperador?.toString() || ''}
              onChangeText={(val) => setIdOperador(val)}
              keyboardType="numeric"
            />
            <TouchableOpacity style={[styles.scannerBtn, { backgroundColor: colors.primary }]} onPress={() => openScanner('operador')}>
              <MaterialCommunityIcons name="barcode-scan" size={24} color="#FFFFFF" />
            </TouchableOpacity>
          </View>
          {idOperador ? (
            <Text style={[styles.operatorDisplayName, { color: colors.primary }]}>
              {listaOperadores.find(o => o.ID == idOperador)?.NOME || 'ID não cadastrado'}
            </Text>
          ) : null}
        </View>

        <TouchableOpacity 
          style={[styles.saveBtn, { backgroundColor: colors.success }, loading && styles.disabledBtn]} 
          onPress={handleSalvar}
          disabled={loading}
        >
          {loading ? <ActivityIndicator color="#FFF" /> : <Text style={styles.saveBtnText}>REGISTRAR INÍCIO</Text>}
        </TouchableOpacity>
      </ScrollView>

      {/* Modal Scanner */}
      <Modal visible={scanning} animationType="slide">
        <CameraView style={{ flex: 1 }} onBarcodeScanned={handleScan} />
        <TouchableOpacity style={styles.closeBtn} onPress={() => setScanning(false)}>
          <Text style={styles.closeBtnText}>Cancelar</Text>
        </TouchableOpacity>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  scrollContent: { padding: 20 },
  header: { fontSize: 26, fontWeight: 'bold' },
  subHeader: { fontSize: 14, marginBottom: 25 },
  formGroup: { marginBottom: 15 },
  label: { fontSize: 12, fontWeight: 'bold', marginBottom: 5, textTransform: 'uppercase' },
  inputWrapper: { flexDirection: 'row' },
  input: {
    flex: 1,
    height: 65,
    borderWidth: 1,
    borderTopLeftRadius: 12,
    borderBottomLeftRadius: 12,
    paddingHorizontal: 15,
    fontSize: 16,
  },
  scannerBtn: {
    width: 70,
    height: 65,
    justifyContent: 'center',
    alignItems: 'center',
    borderTopRightRadius: 12,
    borderBottomRightRadius: 12,
  },
  pickerContainer: {
    height: 65,
    borderRadius: 12,
    borderWidth: 1,
    justifyContent: 'center',
  },
  picker: { height: 65, width: '100%' },
  saveBtn: {
    height: 60,
    borderRadius: 15,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 20,
    elevation: 3,
  },
  saveBtnText: { color: '#FFF', fontWeight: 'bold', fontSize: 18 },
  disabledBtn: { backgroundColor: '#A5D6A7' },
  operatorDisplayName: { fontSize: 13, fontWeight: 'bold', marginTop: 5, fontStyle: 'italic' },
  closeBtn: { position: 'absolute', bottom: 40, alignSelf: 'center', backgroundColor: '#DC3545', padding: 15, borderRadius: 25 },
  closeBtnText: { color: '#FFF', fontWeight: 'bold' },
});
