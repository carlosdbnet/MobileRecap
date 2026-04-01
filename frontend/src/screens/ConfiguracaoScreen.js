import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity, ScrollView, Alert, ActivityIndicator } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { Picker } from '@react-native-picker/picker';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import { auxService } from '../services';
import { useTheme } from '../context/ThemeContext';

export default function ConfiguracaoScreen() {
  const [ip, setIp] = useState('192.168.15.98');
  const [porta, setPorta] = useState('8000');
  const [setor, setSetor] = useState('');
  const [operador, setOperador] = useState('');
  const { dark, colors, mode, setMode } = useTheme();
  
  const [listaSetores, setListaSetores] = useState([]);
  const [listaOperadores, setListaOperadores] = useState([]);
  
  const [loading, setLoading] = useState(false);
  const [tested, setTested] = useState(false);

  useEffect(() => {
    loadSettings();
  }, []);

  const loadSettings = async () => {
    try {
      const savedIp = await AsyncStorage.getItem('server_ip');
      const savedPort = await AsyncStorage.getItem('server_port');
      const savedSetor = await AsyncStorage.getItem('default_setor');
      const savedOperador = await AsyncStorage.getItem('default_operador');

      if (savedIp) setIp(savedIp);
      if (savedPort) setPorta(savedPort);
      if (savedSetor) setSetor(savedSetor);
      if (savedOperador) setOperador(savedOperador);
      
      // Carregar listas se o IP estiver definido
      if (savedIp || ip) {
        fetchAuxiliares(savedIp || ip, savedPort || porta);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const fetchAuxiliares = async (currentIp, currentPort) => {
    try {
      const setores = await auxService.listarSetores();
      const operadores = await auxService.listarOperadores();
      setListaSetores(setores || []);
      setListaOperadores(operadores || []);
      return { success: true };
    } catch (error) {
      console.warn("Não foi possível carregar listas auxiliares:", error);
      return { success: false, error: error.message };
    }
  };

  const testarConexao = async () => {
    const fullUrl = `http://${ip}:${porta}/`;
    
    if (ip.toLowerCase() === 'localhost' || ip === '127.0.0.1') {
      Alert.alert('IP Inválido', 'No celular (APK), você deve usar o IP local do seu computador (ex: 192.168.15.20) e não localhost.');
      return;
    }

    setLoading(true);
    setTested(false);
    try {
      console.log(`Testando conexão em: ${fullUrl}`);
      const response = await axios.get(fullUrl, { timeout: 8000 });
      if (response.status === 200) {
        await AsyncStorage.setItem('server_ip', ip);
        await AsyncStorage.setItem('server_port', porta);
        
        setTested(true);
        const result = await fetchAuxiliares(ip, porta);
        
        if (result.success) {
          Alert.alert('Sucesso', 'Conexão estabelecida e listas carregadas com sucesso!');
        } else {
          Alert.alert('Parcial', 'Conexão estabelecida, mas não foi possível carregar Setores/Operadores. Verifique se o servidor está configurado.');
        }
      }
    } catch (error) {
      console.error(error);
      let errorDetail = error.message;
      
      // Detecção de erro comum de segurança no Android (bloqueio de HTTP)
      if (errorDetail === "Network Error" && !error.response) {
        errorDetail = "Erro de Rede: O Android pode estar bloqueando a conexão HTTP (Cleartext). Verifique se o app foi compilado com a permissão correta ou tente via navegador no celular primeiro.";
      }

      const errorMsg = error.response ? `Erro: ${error.response.status}` : (error.code === 'ECONNABORTED' ? 'Tempo esgotado (Timeout)' : errorDetail);
      
      Alert.alert(
        'Falha na Conexão', 
        `${errorMsg}\n\nURL Testada:\n${fullUrl}\n\nVerifique se o computador e o celular estão no mesmo Wi-Fi.`
      );
    } finally {
      setLoading(false);
    }
  };

  const salvarConfiguracoes = async () => {
    if (!tested) {
      Alert.alert('Atenção', 'Por favor, teste a conexão antes de salvar.');
      return;
    }

    try {
      await AsyncStorage.setItem('server_ip', ip);
      await AsyncStorage.setItem('server_port', porta);
      await AsyncStorage.setItem('default_setor', setor.toString());
      await AsyncStorage.setItem('default_operador', operador.toString());
      
      Alert.alert('Sucesso', 'Configurações salvas!');
    } catch (error) {
      Alert.alert('Erro', 'Falha ao salvar.');
    }
  };

  return (
    <SafeAreaView style={[styles.container, { backgroundColor: colors.background }]}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={[styles.header, { color: colors.text }]}>Configurações</Text>
        <Text style={[styles.subHeader, { color: colors.textSecondary }]}>Ajuste conexão e selecione os padrões.</Text>

        <View style={[styles.section, { backgroundColor: colors.surface }]}>
          <Text style={[styles.sectionTitle, { color: colors.primary }]}>Preferências Visuais</Text>
          <View style={styles.formGroup}>
            <Text style={[styles.label, { color: colors.textSecondary }]}>Tema do Aplicativo</Text>
            <View style={[styles.pickerContainer, { backgroundColor: colors.inputBackground, borderColor: colors.border }]}>
              <Picker
                selectedValue={mode}
                onValueChange={(itemValue) => setMode(itemValue)}
                style={[styles.picker, { color: colors.text }]}
                dropdownIconColor={colors.text}
              >
                <Picker.Item label="Claro" value="light" color={colors.text} />
                <Picker.Item label="Escuro" value="dark" color={colors.text} />
                <Picker.Item label="Seguir Sistema" value="system" color={colors.text} />
              </Picker>
            </View>
          </View>
        </View>

        <View style={[styles.section, { backgroundColor: colors.surface }]}>
          <Text style={[styles.sectionTitle, { color: colors.primary }]}>Conectividade</Text>
          <View style={styles.rowContainer}>
            <View style={[styles.formGroup, { flex: 0.7, marginRight: 10 }]}>
              <Text style={[styles.label, { color: colors.textSecondary }]}>Endereço IP</Text>
              <TextInput 
                style={[styles.input, { backgroundColor: colors.inputBackground, borderColor: colors.border, color: colors.text }]} 
                placeholderTextColor={colors.textSecondary}
                value={ip}
                onChangeText={(text) => { setIp(text); setTested(false); }}
              />
            </View>
            <View style={[styles.formGroup, { flex: 0.3 }]}>
              <Text style={[styles.label, { color: colors.textSecondary }]}>Porta</Text>
              <TextInput 
                style={[styles.input, { backgroundColor: colors.inputBackground, borderColor: colors.border, color: colors.text }]} 
                placeholderTextColor={colors.textSecondary}
                value={porta}
                onChangeText={(text) => { setPorta(text); setTested(false); }}
                keyboardType="numeric"
              />
            </View>
          </View>
          
          <TouchableOpacity 
            style={[styles.testBtn, { backgroundColor: colors.primary }, tested && styles.testBtnSuccess]} 
            onPress={testarConexao}
            disabled={loading}
          >
            {loading ? <ActivityIndicator color="#FFF" /> : <Text style={styles.btnText}>{tested ? "CONEXÃO OK" : "TESTAR CONEXÃO"}</Text>}
          </TouchableOpacity>
        </View>

        <View style={[styles.section, { backgroundColor: colors.surface }]}>
          <Text style={[styles.sectionTitle, { color: colors.primary }]}>Padrões do Aparelho</Text>
          
          <View style={styles.formGroup}>
            <Text style={[styles.label, { color: colors.textSecondary }]}>Setor Padrão</Text>
            <View style={[styles.pickerContainer, { backgroundColor: colors.inputBackground, borderColor: colors.border }]}>
              <Picker
                selectedValue={setor}
                onValueChange={(itemValue) => setSetor(itemValue)}
                style={[styles.picker, { color: colors.text }]}
                dropdownIconColor={colors.text}
              >
                <Picker.Item label="Selecione um Setor..." value="" color={colors.textSecondary} />
                {listaSetores.map(s => (
                  <Picker.Item key={s.id} label={s.descricao} value={s.id} color={colors.text} />
                ))}
              </Picker>
            </View>
          </View>

          <View style={styles.formGroup}>
            <Text style={[styles.label, { color: colors.textSecondary }]}>Operador Padrão</Text>
            <View style={[styles.pickerContainer, { backgroundColor: colors.inputBackground, borderColor: colors.border }]}>
              <Picker
                selectedValue={operador}
                onValueChange={(itemValue) => setOperador(itemValue)}
                style={[styles.picker, { color: colors.text }]}
                dropdownIconColor={colors.text}
              >
                <Picker.Item label="Selecione um Operador..." value="" color={colors.textSecondary} />
                {listaOperadores.map(o => (
                  <Picker.Item key={o.id} label={o.nome} value={o.id} color={colors.text} />
                ))}
              </Picker>
            </View>
          </View>
        </View>

        <TouchableOpacity 
          style={[styles.saveBtn, { backgroundColor: colors.text }, !tested && styles.disabledBtn]} 
          onPress={salvarConfiguracoes}
          disabled={!tested}
        >
          <Text style={[styles.saveBtnText, { color: dark ? '#000' : '#FFF' }]}>SALVAR CONFIGURAÇÕES</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  scrollContent: { padding: 20 },
  header: { fontSize: 26, fontWeight: 'bold' },
  subHeader: { fontSize: 14, marginBottom: 20 },
  section: { borderRadius: 12, padding: 15, marginBottom: 15, elevation: 2 },
  sectionTitle: { fontSize: 16, fontWeight: 'bold', marginBottom: 15 },
  rowContainer: { flexDirection: 'row', justifyContent: 'space-between' },
  formGroup: { marginBottom: 12 },
  label: { fontSize: 11, fontWeight: 'bold', marginBottom: 5, textTransform: 'uppercase' },
  input: { height: 65, borderRadius: 12, borderWidth: 1, paddingHorizontal: 15, fontSize: 16 },
  pickerContainer: { height: 65, borderRadius: 12, borderWidth: 1, justifyContent: 'center' },
  picker: { height: 65, width: '100%' },
  testBtn: { height: 50, borderRadius: 12, justifyContent: 'center', alignItems: 'center', marginTop: 10 },
  testBtnSuccess: { backgroundColor: '#28A745' },
  saveBtn: { height: 55, borderRadius: 12, justifyContent: 'center', alignItems: 'center', marginTop: 10 },
  saveBtnText: { color: '#FFF', fontWeight: 'bold', fontSize: 16 },
  btnText: { color: '#FFF', fontWeight: 'bold' },
  disabledBtn: { backgroundColor: '#ADB5BD' },
});
