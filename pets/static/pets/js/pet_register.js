
function joinBirth() { //Une os selects de mês e ano de nascimento e o transforma em uma data válida para gravação 

  //Pega o mês e ano de nascimento e os une formando uma data válida
  var birthMonth = document.getElementById("birth_month").value;
  var birthYear = document.getElementById("birth_year").value;
  var formattedBirth = birthYear + '-' + birthMonth + '-01'; 

  //Cria um campo invisível, preenche-o com a data válida e retorna-o.
  var birthDateInput = document.createElement('input');
  birthDateInput.type = 'hidden';
  birthDateInput.name = 'birth';  // O nome do campo no Django
  birthDateInput.value = formattedBirth;  // O valor da data formatada
  return birthDateInput;
}

function joinVaccine() {

  //Pega o mês e o ano da última vacinação e forma uma data válida
  var vaccineMonth = document.getElementById("vaccine_month").value;
  var vaccineYear = document.getElementById("vaccine_year").value;
  var formattedVacine = vaccineYear + '-' + vaccineMonth + '-01';
  
  //Cria um campo invisível, preenche-o com a data válida e retorna-o.
  var vaccineDateInput = document.createElement('input');
  vaccineDateInput.type = 'hidden';
  vaccineDateInput.name = 'vaccine';
  vaccineDateInput.value = formattedVacine;
  
  return vaccineDateInput;
}

function joinVermifuge(){

  //Pega o mês e o ano da vermifugação e os junta para criar uma data válida
  var vermifugeMonth = document.getElementById("vermifuge_month").value;
  var vermifugeYear = document.getElementById("vermifuge_year").value;
  var formattedVermifuge = vermifugeYear + '-' + vermifugeMonth + '-01';

  //Cria um campo invisível, preenche-o com a data válida e retorna-o.
  var vermifugeDateInput = document.createElement('input');
  vermifugeDateInput.type = 'hidden';
  vermifugeDateInput.name = 'vermifuge';  // O nome do campo no Django
  vermifugeDateInput.value = formattedVermifuge;  // O valor da data formatada
  return vermifugeDateInput;
}        
 
function submitForm(event) {

  event.preventDefault(); //Impede o envio do formulário

  const form = document.getElementById('dog_register');
  form.appendChild(joinBirth());
  form.appendChild(joinVaccine());
  form.appendChild(joinVermifuge());
  form.submit();
}

//Função que substitui o placeholder por um preview da imagem quando essa é carregada
function previewImage(event, previewId) {
  const input = event.target;
  const preview = document.getElementById(previewId);

  if (input.files && input.files[0]) {
    const reader = new FileReader();

    reader.onload = function(e) {
      preview.src = e.target.result;
      preview.style.display = 'block';
    }

    reader.readAsDataURL(input.files[0]);
  }
}

document.getElementById("dog_register").addEventListener("submit", submitForm);