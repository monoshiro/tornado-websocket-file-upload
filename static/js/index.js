/**
 * Created by Mono on 9/26/2016.
 */

$(document).ready(function () {

    var web_socket = new WebSocket('ws://localhost:8000/ws_index');

    var data = null;
    var file_name = null;

    $(document).on('change', '#file-input', function (e) {
        var file = e.target.files[0];
        file_name = file.name;

        var file_reader = new FileReader();

        file_reader.onload = function (e) {
            data = e.target.result;
        };

        file_reader.readAsDataURL(file);

    });

    $(document).on('click', '#btn-submit', function () {

        var message = {
            'file_name': file_name,
            'data': data
        };

        web_socket.send(JSON.stringify(message));

    })

});
