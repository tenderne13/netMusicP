function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function getRootPath(){
	//pathName:--->   mbuy/user/login.action
	var pathName = window.location.pathname.substring(1);
	//webName:--->mbuy
	var webName = pathName == '' ? '' : pathName.substring(0, pathName.indexOf('/'));
	//return:--->http://localhost:9999/mbuy/
	//return window.location.protocol + '//' + window.location.host + '/'+ webName + '/';
    return window.location.protocol + '//' + window.location.host +'/';
}

