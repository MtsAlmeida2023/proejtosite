document.addEventListener("DOMContentLoaded", function() {

    const offcanvas = new bootstrap.Offcanvas(document.getElementById('searchBackdrop'));
    let num_results_text = document.getElementById("num_results_id").innerText;
    
    if (num_results_text == "Nenhum registro foi encontrado")
        offcanvas.show();

    const fields = document.querySelectorAll('.field-onchange');
    const submitButton = document.getElementById('btn_search');
    let changedField = false;

    console.log(fields);

    fields.forEach(field => {

        field.addEventListener('change', function() {

            changedField = true;
            checkChanges();

        });
    
        if (field.type === 'text') {
            field.addEventListener('input', function() {
    
                changedField = true;    
                checkChanges();

            });
        }
    });

    function checkChanges() {
        submitButton.disabled = !changedField;
    }
});