$(document).ready(function () {
    /* Forma Jquery */
    let user = $("#user");
    /* Forma JS */
    let pass = document.getElementById("pass");
    let rol = $("#optRol");

    /* Ejemplo de JSON construido */
    let login = {
        /* "atributo":"valor" */
        "username": "",
        "password": "",
        "role": ""
    }

    $("#btnCrearCuenta").click(function () {
        $("#btnSub").toggle(500);
        $("#btnRes").toggle(500);
        $("#cuenta").toggle(500);
        $("#logincuenta").toggle(500);
    })

    //Gets de usuario
    const userLogin = document.getElementById("user");
    const passLogin = document.getElementById("pass");
    const formLogin = document.getElementById("formLogin");
    const parrafoLogin = document.getElementById("warningsLogin");

    
    const emailRegistro = document.getElementById("email");
    const passRegistro = document.getElementById("inputPassword4");
    const passConfirmRegistro = document.getElementById("inputPasswordConfirmar");
    const direccionRegistro = document.getElementById("inputAddress");
    const ciudadRegistro = document.getElementById("inputCity");
    const formRegistro = document.getElementById("formRegistro");
    const parrafoRegistro = document.getElementById("warningsRegistro");

    //Bloque funciones de validacion
    function validarEmail(email){
        let regexEmail = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        return regexEmail.test(email);
    }

    //Validad largo minimo de 6 caracteres
    function validarLargo(elemento){
        return elemento.length < 6;
    }


    //Validaciones registros
    //Login
    formLogin.addEventListener("submit", e=>{
        e.preventDefault();
        let warningsLogin = "";
        parrafoLogin.innerHTML = "";
        let entrar = false;
        //console.log(validarLargo(userLogin.value));        
        if(validarLargo(userLogin.value)){
            warningsLogin += 'Nombre usuario debe superar los 6 caracteres <br>';
            entrar = true;
        }

        if(validarLargo(passLogin.value)){
            warningsLogin += 'La contraseña debe superar los 6 caracteres <br>';
            entrar = true;
        }
        
        if(entrar){
            parrafoLogin.innerHTML = warningsLogin;
        } else {
            alert("Ud. ha ingresado correctamente");
        }
        
    });

    //Registro
    formRegistro.addEventListener("submit", e=>{
        e.preventDefault();
        let warningsRegistro = "";
        parrafoRegistro.innerHTML = "";
        let entrar = false;
        if(!validarEmail(emailRegistro.value)){
            warningsRegistro += 'El email no es valido <br>';
            entrar = true;
        }

        if(validarLargo(passRegistro.value)){
            warningsRegistro += 'La contraseña debe superar los 6 caracteres <br>';
            entrar = true;
        }

        if(passRegistro.value !== passConfirmRegistro.value){
            warningsRegistro += 'Las contraseñas deben coincidir <br>';
            entrar = true;
        }

        if(entrar){
            parrafoRegistro.innerHTML = warningsRegistro;
        } else {
            alert("Se ha registrado correctamente");
        }
    });

    // Seleccionar el botón de limpiar campos por su ID
    $("#btnRes").click(function() {
        // Limpiar los campos del formulario
        $("#formLogin")[0].reset(); // Limpiar campos del formulario de login
    });

    $("#botoneRegistro2").click(function() {
        // Limpiar los campos del formulario
        $("#formRegistro")[0].reset(); // Limpiar campos del formulario de registro
    });
});
