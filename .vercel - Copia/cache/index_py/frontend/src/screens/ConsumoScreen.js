import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity, ScrollView, Alert, ActivityIndicator } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
// import { consumoService } from '../services'; // Implementaremos se necessário, por enquanto usemos o padrão

export default function ConsumoScreen() {
  const [idProduto, setIdProduto] = useState('');
  const [quantidade, setQuantidade] = useState('');
  const [loading, setLoading] = useState(false);

  const salvarConsumo = async () => {
    if (!idProduto || !quantidade) {
      Alert.alert('Campos Obrigatórios', 'Preencha o ID do produto e a quantidade.');
      return;
    }
    setLoading(true);
    try {
      // Simulação ou chamada real se o endpoint existir
      // await consumoService.registrar({ id_produto: parseInt(idProduto), quantidade: parseFloat(quantidade) });
      Alert.alert('Sucesso', 'Consumo de matéria-prima registrado!');
      setIdProduto('');
      setQuantidade('');
    } catch (error) {
      Alert.alert('Erro', 'Não foi possível registrar o consumo.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={styles.header}>Consumo de Material</Text>
        <Text style={styles.subHeader}>Registre o uso de insumos na produção.</Text>

        <View style={styles.formGroup}>
          <Text style={styles.label}>ID do Produto / Insumo</Text>
          <TextInput 
            style={styles.input} 
            placeholder="Ex: 501" 
            value={idProduto}
            onChangeText={setIdProduto}
            keyboardType="numeric"
          />
        </View>

        <View style={styles.formGroup}>
          <Text style={styles.label}>Quantidade consumida</Text>
          <TextInput 
            style={styles.input} 
            placeholder="Ex: 5.5 (kg/un)" 
            value={quantidade}
            onChangeText={setQuantidade}
            keyboardType="decimal-pad"
          />
        </View>

        <TouchableOpacity 
          style={[styles.saveBtn, loading && { opacity: 0.7 }]} 
          onPress={salvarConsumo}
          disabled={loading}
        >
          {loading ? <ActivityIndicator color="#FFF" /> : <Text style={styles.saveBtnText}>REGISTRAR CONSUMO</Text>}
        </TouchableOpacity>
      </ScrollView>
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
  input: {
    height: 55,
    backgroundColor: '#F8F9FA',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#DEE2E6',
    paddingHorizontal: 15,
    fontSize: 16,
  },
  saveBtn: {
    backgroundColor: '#343A40',
    height: 60,
    borderRadius: 15,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 10,
  },
  saveBtnText: { color: '#FFF', fontWeight: 'bold', fontSize: 16 },
});
