$(function() {
    $.ajax({
        url: 'http://localhost:5000/listar_pacientes',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listarPacientes,// chama a função listar para processar o resultado
        error: function() {
            alert("Erro ao ler dados! Erro no backend!");
        }
    });

    function listarPacientes (pacientes) {
        // percorrer a lista de pessoas retornadas; 
        for (var i in pacientes) { //i vale a posição no vetor
            novaLinha = '<tr>' + // elabora linha com os dados da pessoa
              '<td>' + pacientes[i].nome + '</td>' + 
              '<td>' + pacientes[i].idade + '</td>' + 
              '<td>' + pacientes[i].email + '</td>' + 
              '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaPacientes').append(novaLinha);
        }
    }
});