document.addEventListener('DOMContentLoaded', function () {

    const email = document.getElementById('email');
    const emailHelp = document.getElementById('emailHelp');
  
    const password = document.getElementById('pwd');
    const confirmPassword = document.getElementById('chk_pwd');
    const pwdHelp = document.getElementById('passwordHelp');

    const submitButton = document.getElementById('btn_registrar');
  
    var passwordValid = false;
    var emailValid = false;

    function validatePasswords() {
      if (confirmPassword.value === password.value) {
        confirmPassword.classList.remove('is-invalid');
        confirmPassword.classList.add('is-valid');
        pwdHelp.classList.add('d-none');
        passwordValid = true;

      } else {
        confirmPassword.classList.remove('is-valid');
        confirmPassword.classList.add('is-invalid');
        pwdHelp.classList.remove('d-none');
      }
      
      submitButton.disabled = !(passwordValid && emailValid);
    
    }
    
    function validateEmail() {
      const isValid = email.checkValidity();
      if (isValid) {
      
        email.classList.remove('is-invalid');
        email.classList.add('is-valid');
        emailHelp.classList.add('d-none');
        emailValid = true;
      
      } else {
        email.classList.remove('is-valid');
        email.classList.add('is-invalid');
        emailHelp.classList.remove('d-none');
      }
      submitButton.disabled = !(passwordValid && emailValid);
    }
  
    password.addEventListener('input', validatePasswords);
    confirmPassword.addEventListener('input', validatePasswords);
    email.addEventListener('input', validateEmail);

  
  
  });
  