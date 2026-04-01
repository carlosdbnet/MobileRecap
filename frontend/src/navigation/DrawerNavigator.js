import React from 'react';
import { View, Alert, BackHandler, StyleSheet, Text } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { 
  createDrawerNavigator, 
  DrawerContentScrollView, 
  DrawerItemList, 
  DrawerItem 
} from '@react-navigation/drawer';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useTheme } from '../context/ThemeContext';

import DashboardScreen from '../screens/DashboardScreen';
import ApontamentoScreen from '../screens/ApontamentoScreen';
import ExameInicialScreen from '../screens/ExameInicialScreen';
import ExameFinalScreen from '../screens/ExameFinalScreen';
import FalhasScreen from '../screens/FalhasScreen';
import MateriaPrimaScreen from '../screens/MateriaPrimaScreen';
import ExpedicaoScreen from '../screens/ExpedicaoScreen';
import BalancoScreen from '../screens/BalancoScreen';
import ConfiguracaoScreen from '../screens/ConfiguracaoScreen';

const Drawer = createDrawerNavigator();

function CustomDrawerContent(props) {
  const { dark, colors } = useTheme();
  const handleSair = () => {
    Alert.alert(
      "Sair do MobCap",
      "Deseja realmente encerrar o aplicativo?",
      [
        { text: "Cancelar", style: "cancel" },
        { 
          text: "Sair", 
          onPress: () => BackHandler.exitApp(),
          style: "destructive" 
        }
      ]
    );
  };

  return (
    <SafeAreaView style={{ flex: 1 }} edges={['bottom', 'left', 'right']}>
      {/* Container principal para dividir ScrollView e Rodapé */}
      <View style={{ flex: 1 }}>
        <DrawerContentScrollView {...props} style={{ flex: 1 }}>
          <View style={[styles.drawerHeader, { backgroundColor: colors.surface, borderBottomColor: colors.border }]}>
            <Text style={[styles.drawerTitle, { color: colors.primary }]}>MobCap</Text>
            <Text style={[styles.drawerSubtitle, { color: colors.textSecondary }]}>Controle de Produção</Text>
          </View>
          <DrawerItemList {...props} />
        </DrawerContentScrollView>
        
        {/* Botão de Sair fixo na base do menu com maior contraste e segurança */}
        <View style={[styles.exitContainer, { borderTopColor: colors.border, backgroundColor: colors.surface }]}>
          <DrawerItem
            label="SAIR DO APLICATIVO"
            icon={({ size }) => (
              <MaterialCommunityIcons name="exit-to-app" color="#FFF" size={24} />
            )}
            onPress={handleSair}
            labelStyle={{ color: '#FFF', fontWeight: 'bold', fontSize: 14 }}
            style={[styles.exitButton, { backgroundColor: colors.error }]}
          />
        </View>
      </View>
    </SafeAreaView>
  );
}

export default function DrawerNavigator() {
  const { colors, dark } = useTheme();
  return (
    <Drawer.Navigator 
      initialRouteName="Dashboard"
      drawerContent={(props) => <CustomDrawerContent {...props} />}
      screenOptions={{
        headerStyle: { backgroundColor: colors.headerBackground },
        headerTintColor: colors.text,
        drawerStyle: { backgroundColor: colors.surface },
        drawerActiveTintColor: colors.primary,
        drawerInactiveTintColor: colors.textSecondary,
      }}
    >
      <Drawer.Screen 
        name="Dashboard" 
        component={DashboardScreen} 
        options={{ 
          title: 'Dashboard',
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="view-dashboard" color={color} size={size} />
        }} 
      />
      <Drawer.Screen 
        name="Apontamento de Serviço" 
        component={ApontamentoScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="clipboard-text" color={color} size={size} />
        }}
      />
      <Drawer.Screen 
        name="Exame Inicial" 
        component={ExameInicialScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="file-search" color={color} size={size} />
        }}
      />
      <Drawer.Screen 
        name="Exame Final" 
        component={ExameFinalScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="check-circle" color={color} size={size} />
        }}
      />
      <Drawer.Screen 
        name="Registro de Falhas" 
        component={FalhasScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="alert-circle" color={color} size={size} />
        }}
      />
      <Drawer.Screen 
        name="Materia Prima" 
        component={MateriaPrimaScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="layers" color={color} size={size} />
        }}
      />
      <Drawer.Screen 
        name="Expedição de Pneus" 
        component={ExpedicaoScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="truck-delivery" color={color} size={size} />
        }}
      />
      <Drawer.Screen 
        name="Balanço de Pneus" 
        component={BalancoScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="scale" color={color} size={size} />
        }}
      />
      <Drawer.Screen 
        name="Configuração" 
        component={ConfiguracaoScreen} 
        options={{ 
          drawerIcon: ({ color, size }) => <MaterialCommunityIcons name="cog" color={color} size={size} />
        }}
      />
    </Drawer.Navigator>
  );
}

const styles = StyleSheet.create({
  drawerHeader: {
    padding: 20,
    marginBottom: 10,
    borderBottomWidth: 1,
  },
  drawerTitle: {
    fontSize: 22,
    fontWeight: 'bold',
  },
  drawerSubtitle: {
    fontSize: 12,
  },
  exitContainer: {
    borderTopWidth: 1,
    paddingTop: 10,
    paddingBottom: 10
  },
  exitButton: {
    borderRadius: 12,
    marginHorizontal: 15,
    backgroundColor: '#DC3545', // Fundo vermelho sólido para máximo destaque
    paddingVertical: 5
  }
});
