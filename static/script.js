const visibilityToggle = Document.querySelector('.visibility');

const input = Document.querySelector('.login input');

var password = true

visibilityToggle.addEventListener('click', function(){
    if(password) {
        password.setAttribute('type', 'text');
        visibilityToggle.innerHTML = 'visibility';
    } else{
        password.setAttribute('type', 'password');
        visibilityToggle.innerHTML = 'visibility_off';
    }
 
});
