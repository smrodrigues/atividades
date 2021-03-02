$(function() {
    function exibirPacientes() {
        $.ajax({
            url: 'http://localhost:5000/listar_pacientes',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listarPacientes,// chama a função listar para processar o resultado
            error: function() {
                alert("Erro ao ler dados! Erro no backend!");
            }
        });
    // ajax é tipo um método do jquery que tem atributos necessários paar fazer requisições em um servidor
        function listarPacientes (pacientes) {
            $("#corpoTabelaPacientes").empty();
            alterarVisibilidade("tabelaPacientes")
            for (var i in pacientes) { //i vale a posição no vetor
                novaLinha = '<tr>' + 
                  '<td>' + pacientes[i].nome + '</td>' + 
                  '<td>' + pacientes[i].idade + '</td>' + 
                  '<td>' + pacientes[i].email + '</td>' + 
                  '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaPacientes').append(novaLinha);
            }
        }
    }

    function alterarVisibilidade(identificador) {
        $("#tabelaPacientes").addClass("d-none");
        $("#conteudoInicial").addClass("d-none");
        $(`#${identificador}`).removeClass("d-none");
    }

    $(document).on("click","#linkListarPacientes", function() {
        exibirPacientes();
    });

    $(document).on("click","#linkInicio", function() {
        alterarVisibilidade("conteudoInicial");
    });

    $(document).on("click", "#btnIncluirPaciente", function() {
        nome = $("#campoNomePaciente").val();
        idade = $("#campoIdadePaciente").val();
        email = $("#campoEmailPaciente").val();

        var dados = JSON.stringify({
            nome: nome,
            idade: idade,
            email: email,
        });

        $.ajax({
            url: 'http://localhost:5000/incluir_paciente',
            method: 'POST',
            dataType: 'json',
            contentType: 'application/json', 
            data: dados, 
            success: incluirPaciente,
            error: erroAoIncluir,
        });

        function incluirPaciente(retorno) {
            if(retorno.resultado==="ok") {
                alert("Paciente incluído com sucesso!!!");

                $("#campoNomePaciente").val("");
                $("#campoIdadePaciente").val("");
                $("#campoEmailPaciente").val("");
            }else {
                alert(`${retorno.resultado}: ${retorno.detalhes}`);    
            }
        }

        function erroAoIncluir(retorno) {
            alert(`${retorno.resultado}: ${retorno.detalhes}`);
        }
    });

    $('#modalIncluirPaciente').on('hide.bs.modal', function (e) {
        if (! $("#tabelaPaciente").hasClass('d-none')) {
            exibirPacientes();
        }
    });

    alterarVisibilidade("conteudoInicial");
});