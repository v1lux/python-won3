function myForm() {
    let nume = document.getElementById('nume').value;
    let email = document.getElementById('email').value;
    let subiect = document.getElementById('subiect').value;
    let comentariu = document.getElementById('comentariu').value;

    let mesaj_nume = document.getElementById('mesaj_nume');
    let mesaj_email = document.getElementById('mesaj_email');
    let mesaj_subiect = document.getElementById('mesaj_subiect');
    let mesaj_comentariu = document.getElementById('mesaj_comentariu');

    mesaj_nume.innerText = "";
    mesaj_email.innerText = "";
    mesaj_subiect.innerText = "";
    mesaj_comentariu.innerText = "";

    if (nume == "") {
        mesaj_nume.innerText = 'introduceti numele';
        mesaj_nume.style.color = 'red';
    }
    if (email == "") {
        mesaj_email.innerText = 'introduceti adresa de email';
        mesaj_email.style.color = 'red';
    }
    if (subiect == "") {
        mesaj_subiect.innerText = 'introduceti subiectul';
        mesaj_subiect.style.color = 'red';
    }
    if (comentariu == "") {
        mesaj_comentariu.innerText = 'introduceti comentariul';
        mesaj_comentariu.style.color = 'red';
    }
}