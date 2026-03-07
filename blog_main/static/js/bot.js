// Minimal chat widget behavior: toggle, send, display
(function(){
  function qs(id){ return document.getElementById(id); }

  import { marked } from 'https://cdnjs.cloudflare.com/ajax/libs/marked/16.3.0/lib/marked.esm.js';

  const socket = new WebSocket('ws://' + window.location.host + '/ws/sockets/');
  const fullText = document.body.innerText;
  
  var container = document.getElementById('chat-bot-container');
  if(!container) return;
  var toggle = qs('chat-toggle');
  var windowEl = qs('chat-window');
  var closeBtn = qs('chat-close');
  var sendBtn = qs('chat-send');
  var input = qs('chat-input');
  var messages = qs('chat-messages');
  
  socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    dataMsg = marked.parse(data.message);
    appendMessage(dataMsg, 'bot');
    console.log("Message from server:", data.message);
    };

  sendBtn.addEventListener('click', ()=>{
    var val = input.value.trim();
    if(!val) return;

    socket.send(JSON.stringify({'message': val,'page_data': fullText}));
    appendMessage(val, 'user');
    input.value = '';
  });
  

  function openChat(){
    container.classList.remove('chat-bot-closed');
    toggle.setAttribute('aria-expanded','true');
    toggle.classList.add('chat-toggle-close')
    windowEl.setAttribute('aria-hidden','false');
    input.focus();
  }

  function closeChat(){
    container.classList.add('chat-bot-closed');
    toggle.setAttribute('aria-expanded','false');
    windowEl.setAttribute('aria-hidden','true');
    toggle.classList.remove('chat-toggle-close')
  }

  toggle.addEventListener('click', function(){
    if(container.classList.contains('chat-bot-closed')) openChat(); else closeChat();
  });
  closeBtn.addEventListener('click', closeChat);

  function appendMessage(text, who){
    var wrap = document.createElement('div');
    wrap.className = 'chat-message ' + (who||'bot');
    var bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text;
    wrap.appendChild(bubble);
    messages.appendChild(wrap);
    messages.scrollTop = messages.scrollHeight;
  }

//   function send(){
//     var val = input.value.trim();
//     if(!val) return;
//     appendMessage(val, 'user');
//     input.value = '';
//     // placeholder bot reply — replace with real API/socket calls
//     setTimeout(function(){ appendMessage('Thanks — I received: "' + val + '"'); }, 600);
//   }

  sendBtn.addEventListener('click', send);
  input.addEventListener('keydown', function(e){
    if(e.key === 'Enter' && !e.shiftKey){ e.preventDefault(); send(); }
  });

})();
