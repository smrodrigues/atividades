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
            alterarVisibilidade("pacientes")
            for (var i in pacientes) { //i vale a posição no vetor
                novaLinha = `<tr id="linha_${pacientes[i].id}">` + 
                  '<td>' + pacientes[i].nome + '</td>' + 
                  '<td>' + pacientes[i].idade + '</td>' + 
                  '<td>' + pacientes[i].email + '</td>' + 
                  `<td><a href=# id="${pacientes[i].id}" class="excluir_paciente">` +
                        '<p class="badge badge-danger">Excluir</p>' +
                    '</a>' +
                  '</td>' +
                  '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaPacientes').append(novaLinha);
            }
        }
    }

    function exibirMedicos() {
        $.ajax({
            url: 'http://localhost:5000/listar_medicos',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listarMedicos,// chama a função listar para processar o resultado
            error: function() {
                alert("Erro ao ler dados! Erro no backend!");
            }
        });
    // ajax é tipo um método do jquery que tem atributos necessários paar fazer requisições em um servidor
        function listarMedicos (medicos) {
            $("#corpoTabelaMedicos").empty();
            alterarVisibilidade("medicos")
            for (var i in medicos) { //i vale a posição no vetor
                novaLinha = `<tr id="linha_${medicos[i].id}">` + 
                  '<td>' + medicos[i].nome + '</td>' + 
                  '<td>' + medicos[i].idade + '</td>' + 
                  '<td>' + medicos[i].email + '</td>' + 
                  '<td>' + medicos[i].tipo_sanguineo + '</td>' + 
                  '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaMedicos').append(novaLinha);
            }
        }
    }

    function exibirReceitas() {
        $.ajax({
            url: 'http://localhost:5000/listar_receitas',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listarReceitas,// chama a função listar para processar o resultado
            error: function() {
                alert("Erro ao ler dados! Erro no backend!");
            }
        });
    // ajax é tipo um método do jquery que tem atributos necessários paar fazer requisições em um servidor
        function listarReceitas (receitas) {
            $("#corpoTabelaReceitas").empty();
            alterarVisibilidade("receitas")
            for (var i in receitas) { //i vale a posição no vetor
                novaLinha = `<tr id="linha_${receitas[i].id}">` + 
                  '<td>' + receitas[i].codigo + '</td>' + 
                  '<td>' + receitas[i].paciente.nome + '</td>' + 
                  '<td>' + receitas[i].paciente.idade + '</td>' + 
                  '<td>' + receitas[i].paciente.email + '</td>' + 
                  '<td>' + receitas[i].medico.nome + '</td>' + 
                  '<td>' + receitas[i].medico.idade + '</td>' + 
                  '<td>' + receitas[i].medico.email + '</td>' + 
                  '<td>' + receitas[i].medico.tipo_sanguineo + '</td>' + 
                  '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaReceitas').append(novaLinha);
            }
        }
    }

    function alterarVisibilidade(identificador) {
        $("#pacientes").addClass("d-none");
        $("#medicos").addClass("d-none");
        $("#receitas").addClass("d-none");
        $("#conteudoInicial").addClass("d-none");
        $(`#${identificador}`).removeClass("d-none");
    }

    $(document).on("click","#linkListarPacientes", function() {
        exibirPacientes();
    });
    $(document).on("click","#linkListarMedicos", function() {
        exibirMedicos();
    });
    $(document).on("click","#linkListarReceitas", function() {
        exibirReceitas();
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

    $(document).on("click", ".excluir_paciente", function() {
        var componente_clicado = $(this).attr('id');

        $.ajax({
            url: `http://localhost:5000/excluir_paciente/${componente_clicado}`,
            type: 'DELETE',
            dataType: 'json',
            success: excluirPaciente,
            error: erroAoExcluir
        });

        function excluirPaciente(retorno) {
            if (retorno.resultado === "ok") {
                console.log(retorno);
                $("#linha_" + componente_clicado).fadeOut(1000, function(){ //fade.out faz desaparecer "lentamente" (1 segundo)
                    alert("Paciente removido com sucesso!");
                });
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoExcluir (retorno) {
            alert("Erro ao excluir paciente! Erro no Backend! ");
        }
    });

    alterarVisibilidade("conteudoInicial");
});

