const detalhesBtns = document.querySelectorAll('.detalhes-btn');
const detalhesDiv = document.getElementById('produto-detalhes');
const descricaoProduto = document.getElementById('descricao-produto');
const fecharDetalhes = document.getElementById('fechar-detalhes');

detalhesBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const descricao = btn.getAttribute('data-descricao');
        descricaoProduto.textContent = descricao;
        detalhesDiv.classList.add('visible');
    });
});

fecharDetalhes.addEventListener('click', () => {
    detalhesDiv.classList.remove('visible');
});
