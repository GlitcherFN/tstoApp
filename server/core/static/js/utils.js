window.pu = (function() {
  var _txt = 'OK!';

  var _template = '';

  var _divMessage;

  function view(obj) {
    if (typeof obj === 'object') {
      _txt = obj.txt !== undefined ? obj.txt : 'OK!';
    }else if (typeof obj === 'string'){
      _txt = obj;
    }
    showMessage();
  }

  function showMessage() {
    _divMessage = document.createElement('div');
    var divMessage_txt_ = document.createElement('div');

    _divMessage.classList.add('message');
    divMessage_txt_.classList.add('message_txt');

    divMessage_txt_.innerText = _txt;

    _divMessage.appendChild(divMessage_txt_);
    document.body.appendChild(_divMessage);

    killMessage();
  }

  function killMessage() {
    setTimeout(function() {
      _divMessage.remove();
      _divMessage = '';
    }, 3500);
  }

  return {
    show: view,
  }
})();