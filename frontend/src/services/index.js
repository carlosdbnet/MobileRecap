import api from './api';

export const dashboardService = {
  getStats: async () => {
    const { data } = await api.get('/dashboard');
    return data;
  },
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
  buscarPneu: async (codigo_barra) => {
    const { data } = await api.get(`/exames/pneu/${codigo_barra}`);
    return data;
  },
  atualizarStatus: async (codigo_barra, status) => {
    const { data } = await api.put(`/exames/pneu/${codigo_barra}/status?status=${status}`);
    return data;
  },
};

export const falhaService = {
  listarCatalogo: async () => {
    const { data } = await api.get('/falhas');
    return data;
  },
  registrar: async (falha) => {
    const { data } = await api.post('/falhas/registros', falha);
    return data;
  },
};

export const auxService = {
  listarSetores: async () => {
    const { data } = await api.get('/auxiliares/setores');
    return data;
  },
  listarOperadores: async () => {
    const { data } = await api.get('/auxiliares/operadores');
    return data;
  },
};

export const expedicaoService = {
  registrar: async (expedicao) => {
    const { data } = await api.post('/expedicao', expedicao);
    return data;
  },
};
