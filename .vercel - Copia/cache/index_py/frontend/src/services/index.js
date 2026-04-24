import api from './api';

export const dashboardService = {
  getStats: async () => {
    const { data } = await api.get('/dashboard');
    return data;
  },
};

export const setorService = {
  listar: async () => {
    const { data } = await api.get('/setores');
    return data;
  },
  criar: async (setor) => {
    const { data } = await api.post('/setores', setor);
    return data;
  },
};

export const operadorService = {
  listar: async () => {
    const { data } = await api.get('/operadores');
    return data;
  },
  criar: async (operador) => {
    const { data } = await api.post('/operadores', operador);
    return data;
  },
};

export const pneuService = {
  listar: async (query = '') => {
    const { data } = await api.get(`/pneus?q=${query}`);
    return data;
  },
  criar: async (pneu) => {
    const { data } = await api.post('/pneus', pneu);
    return data;
  },
};

export const servicoService = {
  listar: async () => {
    const { data } = await api.get('/servicos');
    return data;
  },
  criar: async (servico) => {
    const { data } = await api.post('/servicos', servico);
    return data;
  },
};

export const medidaService = {
  listar: async () => {
    const { data } = await api.get('/medidas');
    return data;
  },
};

export const desenhoService = {
  listar: async () => {
    const { data } = await api.get('/desenhos');
    return data;
  },
};

// ... Manter os antigos se necessário para não quebrar telas existentes temporariamente
// Antigo auxService para compatibilidade com as telas de Configuração e Apontamento
export const auxService = {
  listarSetores: async () => setorService.listar(),
  listarOperadores: async () => operadorService.listar(),
};

export const producaoService = {
  listar: async () => {
    const { data } = await api.get('/apontamento');
    return data;
  },
  criar: async (apontamento) => {
    const { data } = await api.post('/apontamento', apontamento);
    return data;
  },
};
