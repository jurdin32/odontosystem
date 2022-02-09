function listarPaciente() {
    $.ajax({
        url: "/paciente/listar/",
        type: "get",
        dataType: "json",
        success: function (response) {
            console.log(response);
            $('#tb_listar_paciente tbody').html("");
            for (let i=0; i < response.length; i++){
                let fila = '<tr>';
                 fila += '<td>' + (i+1) + '</td>';
                fila += '<td>' + response[i]["fields"]['cedula'] + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['apellido'] + '</td>';
                fila += '<td>' + response[i]["fields"]['direccion'] + '</td>';
                fila += '<td>' + response[i]["fields"]['ocupacion'] + '</td>';
                fila += '<td>' + response[i]["fields"]['telefono'] + '</td>';
                fila += '</tr>';
                $('#tb_listar_paciente tbody').append(fila);
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}

$(document).ready(function () {
    listarPaciente();
});