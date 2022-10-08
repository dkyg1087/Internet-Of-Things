var socket = new WebSocket('ws://172.16.109.23:12346');
window.addEventListener('load', (event) => {
    try{
        socket.addEventListener('open', (event) => {
            socket.send('Hello Server!');
        });
        socket.addEventListener('message', (event) => {
            alert('Message from server ', event.data);
        });
    }
    catch(err){
        alert(' Socket connection failed, please reload')
    }
  });

//socket.send('Hello Server!');
//   socket.send('Hello Server!');