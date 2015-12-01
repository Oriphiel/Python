/**
 * Created by Arturo Haas on 14/10/2015.
 */
function falta(hora,minuto,id) {
    var ahorita = new Date();
    var fecha = "";
    fecha = ahorita.getMonth() + 1 + '/';
    fecha += ahorita.getDate() + '/';
    fecha += ahorita.getFullYear() + ' ';
    fecha +=hora;
    fecha += ':';
    fecha += minuto+' GMT-0500';
    var deadline = new Date(fecha);
    var diff = deadline - ahorita;
    var diff_seg = Math.floor(diff / 1000);
    var seg = diff_seg % 60;
    var min = Math.floor(diff_seg / 60) % 60;
    var hr = Math.floor(diff_seg / 3600);
    if (hr < 0 || min < 0 || seg < 0) {
        document.getElementById(id).innerHTML = 'Sonada';
    } else {
        document.getElementById(id).innerHTML = doscaracteres(hr) + ':' + doscaracteres(min) + ':' + doscaracteres(seg);
    }
}
function doscaracteres(numero) {
    if (String(numero).length == 1)
        return "0" + numero;
    return numero;
}