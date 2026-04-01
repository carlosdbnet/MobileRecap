import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity, ScrollView, Alert, Modal, FlatList, ActivityIndicator } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { CameraView, useCameraPermissions } from 'expo-camera';
import { falhaService, producaoService } from '../services';

export default function FalhasScreen() {
  const [codigoBarra, setCodigoBarra] = useState('');
  const [loading, setLoading] = useState(false);
  const [scanning, setScanning] = useState(false);
  const [catalogo, setCatalogo] = useState([]);
  const [falhaSelecionada, setFalhaSelecionada] = useState(null);
  const [observacao, setObservacao] = useState('');
  const [permission, requestPermission] = useCameraPermissions();

  useEffect(() => {
    fetchCatalogo();
  }, []);

  const fetchCatalogo = async () => {
    try {
      const data = await falhaService.listarCatalogo();
      setCatalogo(data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleScan = ({ data }) => {
    setCodigoBarra(data);
    setScanning(false);
  };

  const registrarFalha = async () => {
    if (!codigoBarra || !falhaSelecionada) {
      Alert.alert('Atenção', 'Selecione o pneu e o tipo de falha.');
      return;
    }

    setLoading(true);
    try {
      const pneu = await producaoService.buscarPneu(codigoBarra);
      
      const registro = {
        codigo_barra: codigoBarra,
        id_pneu: pneu.id,
        id_setor: 1, // Exemplo: Setor de Triagem
        id_operdor: 1, 
        id_falha: falhaSelecionada.id,
        data: new Date().toISOString().split('T')[0],
        observacao: observacao
      };

      await falhaService.registrar(registro);
      Alert.alert('Sucesso', 'Falha registrada no pneu!');
      setCodigoBarra('');
      setFalhaSelecionada(null);
      setObservacao('');
    } catch (error) {
      console.error(error);
      Alert.alert('Erro', 'Falha ao registrar ocorrência.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={styles.header}>Registrar Falha</Text>
        <Text style={styles.subHeader}>Identifique defeitos técnicos no pneu.</Text>

        <View style={styles.formGroup}>
          <Text style={styles.label}>Pneu (Código de Barras)</Text>
          <View style={styles.inputWrapper}>
            <TextInput 
              style={styles.input} 
              placeholder="Escaneie o pneu" 
              value={codigoBarra}
              onChangeText={setCodigoBarra}
            />
            <TouchableOpacity style={styles.scanBtn} onPress={() => setScanning(true)}>
              <MaterialCommunityIcons name="barcode-scan" size={24} color="#FFF" />
            </TouchableOpacity>
          </View>
        </View>

        <View style={styles.formGroup}>
          <Text style={styles.label}>Tipo de Falha</Text>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.catalogoList}>
            {catalogo.map((item) => (
              <TouchableOpacity 
                key={item.id} 
                style={[styles.falhaCard, falhaSelecionada?.id === item.id && styles.falhaCardActive]}
                onPress={() => setFalhaSelecionada(item)}
              >
                <MaterialCommunityIcons 
                  name="alert-rhombus" 
                  size={24} 
                  color={falhaSelecionada?.id === item.id ? "#FFF" : "#F44336"} 
                />
                <Text style={[styles.falhaCardText, falhaSelecionada?.id === item.id && styles.falhaCardTextActive]}>
                  {item.descricao}
                </Text>
              </TouchableOpacity>
            ))}
          </ScrollView>
        </View>

        <View style={styles.formGroup}>
          <Text style={styles.label}>Observações Técnicas</Text>
          <TextInput 
            style={[styles.input, { height: 100, textAlignVertical: 'top', paddingTop: 15 }]} 
            placeholder="Detalhes sobre a falha..." 
            multiline
            value={observacao}
            onChangeText={setObservacao}
          />
        </View>

        <TouchableOpacity 
          style={[styles.saveBtn, loading && { opacity: 0.7 }]} 
          onPress={registrarFalha}
          disabled={loading}
        >
          {loading ? <ActivityIndicator color="#FFF" /> : <Text style={styles.saveBtnText}>REGISTRAR OCORRÊNCIA</Text>}
        </TouchableOpacity>
      </ScrollView>

      <Modal visible={scanning} animationType="fade">
        <CameraView style={styles.camera} onBarcodeScanned={handleScan} />
        <TouchableOpacity style={styles.closeBtn} onPress={() => setScanning(false)}>
          <Text style={styles.closeBtnText}>Fechar</Text>
        </TouchableOpacity>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FFFFFF' },
  scrollContent: { padding: 25 },
  header: { fontSize: 28, fontWeight: 'bold', color: '#212529' },
  subHeader: { fontSize: 16, color: '#6C757D', marginBottom: 30 },
  formGroup: { marginBottom: 25 },
  label: { fontSize: 14, fontWeight: '600', color: '#495057', marginBottom: 10, textTransform: 'uppercase' },
  inputWrapper: { flexDirection: 'row' },
  input: {
    flex: 1,
    height: 55,
    backgroundColor: '#F8F9FA',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#DEE2E6',
    paddingHorizontal: 15,
  },
  scanBtn: {
    width: 60,
    backgroundColor: '#007AFF',
    justifyContent: 'center',
    alignItems: 'center',
    borderTopRightRadius: 10,
    borderBottomRightRadius: 10,
    marginLeft: -10,
  },
  catalogoList: { paddingVertical: 10 },
  falhaCard: {
    width: 140,
    height: 100,
    backgroundColor: '#FFF',
    borderWidth: 1.5,
    borderColor: '#E9ECEF',
    borderRadius: 15,
    padding: 15,
    marginRight: 15,
    justifyContent: 'center',
    alignItems: 'center',
  },
  falhaCardActive: { backgroundColor: '#F44336', borderColor: '#F44336' },
  falhaCardText: { fontSize: 13, fontWeight: 'bold', color: '#495057', marginTop: 8, textAlign: 'center' },
  falhaCardTextActive: { color: '#FFF' },
  saveBtn: {
    backgroundColor: '#F44336',
    height: 60,
    borderRadius: 15,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 10,
  },
  saveBtnText: { color: '#FFF', fontWeight: 'bold', fontSize: 16 },
  camera: { flex: 1 },
  closeBtn: { position: 'absolute', bottom: 40, alignSelf: 'center', backgroundColor: '#343A40', padding: 15, borderRadius: 25 },
  closeBtnText: { color: '#FFF', fontWeight: 'bold' },
});
