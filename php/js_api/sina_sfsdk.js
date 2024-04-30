var xh5_define, KKE = KKE || {};
~function(n) {
    "use strict";
    function e(n, e, t) {
        if (!u.isStr(n))
            return void u.err(t, [i.CMD_UNEXIST, n].join(":"));
        e = e || {};
        var r = n.split(".")
          , o = r.splice(r.length - 1, r.length).join("")
          , a = r.splice(r.length - 1, r.length).join("")
          , l = r.splice(0, r.length)
          , s = l.join(".")
          , c = [s, a].join(".");
        d.relyCall(c, function() {
            var r = d.modsTree
              , s = void 0;
            do {
                var c = l.shift();
                if (s = s ? s[c] : r[c],
                !s)
                    return void u.err(t, [i.MOD_ERR, a].join(":"))
            } while (l.length);
            var f = s[a] || {}
              , h = f.entity || {}
              , m = h[o];
            "undefined" == typeof m ? u.err(t, [i.CMD_UNEXIST, n].join(":")) : u.isFunc(m) ? m(e, t) : u.isFunc(t) && t(m)
        }, e.modUrl || null)
    }
    for (var t, r, i = {
        SDK_REG: new RegExp("sf_sdk.js",a),
        isLocal: !1,
        isDebug: !1,
        isSSL: !0,
        custom_mod_url: void 0,
        MOD_URL: "js/$moduleName.js",
        MOD_URL_PROD: "http://finance.sina.com.cn/sinafinancesdk/js/$moduleName.js",
        MOD_URL_PROD_S: "https://finance.sina.com.cn/sinafinancesdk/js/$moduleName.js",
        getModUrl: function() {
            return this.custom_mod_url ? this.custom_mod_url + "/$moduleName.js" : this.isLocal ? this.MOD_URL : this.isSSL ? this.MOD_URL_PROD_S : this.MOD_URL_PROD
        },
        CMD_404: "error occured while loading",
        CMD_UNEXIST: "calling nonexistent API",
        MOD_ERR: "erroneous module",
        MOD_DEF_ERR: "illegal module",
        DEP_ERR: "error def module"
    }, o = document.getElementsByTagName("script"), a = o.length; a--; )
        if (t = o[a],
        r = t.src || "",
        i.SDK_REG.test(r)) {
            for (var l, s = t.attributes.length; s--; )
                l = t.attributes[s],
                "ssl" == l.name && (i.isSSL = "true" == l.value),
                "debug" == l.name && (i.isDebug = "true" == l.value),
                "local" == l.name && (i.isLocal = "true" == l.value),
                "murl" == l.name && (i.custom_mod_url = l.value);
            break
        }
    0 == location.protocol.indexOf("https:") && (i.isSSL = !0);
    var u = new function() {
        function n(n, e, t, r) {
            var i = !1
              , o = document.createElement("script")
              , a = document.getElementsByTagName("script")[0]
              , l = document.head || document.getElementsByTagName("head")[0] || document.documentElement
              , s = l.getElementsByTagName("base")[0];
            o.charset = r || "gb2312",
            o.src = n,
            o.async = !0,
            o.onload = o.onreadystatechange = function() {
                i || o.readyState && !/loaded|complete/.test(String(o.readyState)) || (i = !0,
                o.onload = o.onreadystatechange = o.onerror = null,
                o.parentNode.removeChild(o),
                o = null,
                "function" == typeof e && e())
            }
            ,
            o.onerror = function() {
                o.onload = o.onreadystatechange = o.onerror = null,
                o.parentNode.removeChild(o),
                o = null,
                "function" == typeof t && t()
            }
            ,
            a.parentNode ? a.parentNode.insertBefore(o, a) : s ? l.insertBefore(o, s) : l.appendChild(o)
        }
        this.fBind = function(n, e) {
            var t = Array.prototype.slice.call(arguments, 2);
            return function() {
                return n.apply(e, t.concat(Array.prototype.slice.call(arguments)))
            }
        }
        ;
        var e = function(n) {
            return function(e) {
                return {}.toString.call(e) == "[object " + n + "]"
            }
        };
        this.isStr = e("String"),
        this.isFunc = e("Function"),
        this.isArr = e("Array"),
        this.trace = function(n) {
            return {
                log: function() {
                    n && n.log && n.log.apply(n, arguments)
                },
                error: function() {
                    n && n.error && n.error.apply(n, arguments)
                }
            }
        }(null),
        this.err = function(n, e) {
            this.isFunc(n) && n({
                msg: e,
                data: null
            }),
            this.trace.error(e)
        }
        ,
        this.load = n
    }
      , c = ["datas.hq", "datas.k", "datas.t", "utils.util"]
      , d = new function() {
        function n(n, e, r) {
            if (3 != arguments.length)
                return void u.trace.error(i.MOD_DEF_ERR, n);
            var o = t(n)
              , a = o[0]
              , s = o[1]
              , c = a[s];
            c ? c.init = !0 : c = a[s] = {
                init: !0,
                name: n,
                funcQ: [],
                entity: void 0
            },
            u.isStr(e) && (e = [e]);
            for (var d, h = e.length; h--; )
                if (d = e[h],
                d.indexOf("*") > -1) {
                    e.splice(h, 1);
                    var m = d.split(".");
                    m.splice(m.length - 1, m.length);
                    var g = m.join(".");
                    e = e.concat(f(g, n));
                    break
                }
            l(e, e.slice(0), c, r)
        }
        var e = {}
          , t = function(n) {
            for (var t, r = n.split("."), i = r.splice(r.length - 1, r.length).join(""), o = r.splice(0, r.length), a = o.join("."), l = void 0; o.length; ) {
                var s = o.shift();
                l ? (t = l[s],
                t || (t = l[s] = {})) : (t = e[s],
                t || (t = e[s] = {})),
                l = t
            }
            return [l, i, a]
        }
          , r = function(n) {
            for (; n.funcQ.length; ) {
                var e = n.funcQ.shift();
                u.isFunc(e) && e()
            }
        }
          , o = function(n) {
            if (!n)
                return null;
            for (var t = [], r = [], o = 0, a = n.length; a > o; o++) {
                for (var l, s = n[o].split("."), c = void 0; s.length; )
                    if (l = s.shift(),
                    c = c ? c[l] : e[l],
                    !c) {
                        u.trace.error(i.DEP_ERR, s.toString());
                        break
                    }
                r.push(c.entity),
                t.push(l)
            }
            return {
                n: t,
                e: r
            }
        }
          , a = function(n, t, i) {
            var a = t.toString()
              , l = 0 == a.indexOf("function");
            if (l) {
                var s = o(i)
                  , c = t.apply(null, s.e.concat(e));
                n.entity = u.isFunc(c) ? new c : c
            } else
                n.entity = t;
            r(n)
        }
          , l = function(n, e, t, r) {
            e.length ? h(e.shift(), u.fBind(l, this, n, e, t, r)) : a(t, r, n)
        }
          , s = function(n, e, t) {
            e = e.replace(/\./g, "/"),
            t && (t += "$moduleName.js");
            var r = t || i.getModUrl();
            u.load(r.replace("$moduleName", e), null, u.fBind(u.trace.error, this, i.CMD_404, n.name))
        }
          , d = function(n, e) {
            u.isArr(n) && (n = n.join("."));
            var r = t(n)
              , i = r[0]
              , o = r[1]
              , a = i[o];
            return a || (a = {
                init: !1,
                name: n,
                funcQ: [],
                entity: void 0
            },
            i[o] = a,
            s(a, n, e)),
            a
        }
          , f = function(n, e) {
            for (var t, r = [], i = c.length; i--; )
                t = c[i],
                0 == t.indexOf(n) && -1 == t.indexOf(e) && (r[r.length] = t);
            return r
        }
          , h = function(n, e, t) {
            var r = d(n, t);
            u.isFunc(e) && (r.init ? e() : r.funcQ.push(e))
        };
        this.modsTree = e,
        this.relyCall = h,
        xh5_define = n
    }
    ;
    n.api = e,
    n.cls = {},
    n.istLL = "KKE|1.0.4|WANGXuan|SinaFinance|wangxuan2@staff.sina.com.cn"
}(KKE);
;xh5_define("utils.util", [], function() {
    return function() {
        function t(t, e) {
            var i = k(e.prototype);
            i.constructor = t,
            t.prototype = i
        }
        function e() {
            this.evtObj = {}
        }
        function i(t, e) {
            var i = Array.prototype.slice.call(arguments, 2);
            return function() {
                return t.apply(e, i.concat(Array.prototype.slice.call(arguments)))
            }
        }
        function n() {
            return Date.now ? Date.now() : (new Date).getTime()
        }
        function r(t, e) {
            e || (t = t.toLowerCase());
            for (var i, n = 1315423911, r = t.length; r--; )
                i = t.charCodeAt(r),
                n ^= (n << 5) + i + (n >> 2);
            return 2147483647 & n
        }
        function a(t, e, i, n) {
            var r = !1
              , a = document.createElement("script")
              , o = document.getElementsByTagName("script")[0]
              , s = document.head || document.getElementsByTagName("head")[0] || document.documentElement
              , l = s.getElementsByTagName("base")[0];
            n = n || {},
            a.charset = n.charset || "gb18030",
            a.src = t,
            a.type = "text/javascript",
            a.onload = a.onreadystatechange = function() {
                r || a.readyState && !/loaded|complete/.test(a.readyState) || (r = !0,
                a.onload = a.onreadystatechange = a.onerror = null,
                a.parentNode.removeChild(a),
                "function" == typeof e && e())
            }
            ,
            a.onerror = function() {
                a.onload = a.onreadystatechange = a.onerror = null,
                a.parentNode.removeChild(a),
                "function" == typeof i && i()
            }
            ,
            o.parentNode ? o.parentNode.insertBefore(a, o) : l ? s.insertBefore(a, l) : s.appendChild(a)
        }
        function o() {
            function t(t) {
                var e = t.style;
                for (var i in e)
                    e.hasOwnProperty(i) && (t.dom.style[i] = e[i])
            }
            function e() {
                for (var t = ["@keyframes KKELoading", "@-webkit-keyframes KKELoading", "@-moz-keyframes KKELoading"], e = 0, i = t.length; i > e; e++)
                    u.cssUtil.inject(t[e] + l.scaleY)
            }
            function i() {
                if (e(),
                !r) {
                    r = u.$C("div"),
                    t({
                        dom: r,
                        style: l.ctn
                    });
                    for (var i = .1, n = 0, a = l.color.length; a > n; n++) {
                        var o = u.$C("span");
                        t({
                            dom: o,
                            style: l.item
                        });
                        var s = u.clone(l.delay, s)
                          , c = -1 + i * n + "s";
                        for (var d in s)
                            s.hasOwnProperty(d) && (s[d] = c);
                        t({
                            dom: o,
                            style: s
                        }),
                        o.style.background = l.color[n],
                        r.appendChild(o)
                    }
                }
            }
            function n() {
                clearTimeout(o),
                o = setTimeout(function() {
                    "none" != r.style.display && (r.style.display = "none")
                }, 9e3)
            }
            var r, a, o, s, l = {
                ctn: {
                    width: "40px",
                    height: "30px",
                    margin: 0,
                    display: "none",
                    position: "absolute",
                    zIndex: 1
                },
                item: {
                    display: "inline-block",
                    width: "4px",
                    height: "30px",
                    margin: "0px 2px",
                    borderRadius: "5px",
                    animation: "KKELoading 1.2s infinite",
                    webkitAnimation: "KKELoading 1.2s infinite",
                    MozAnimation: "KKELoading 1.2s infinite"
                },
                color: ["#FF5472", "#FF706E", "#FF8762", "#FFAF4C", "#FFD53E"],
                delay: {
                    animationDelay: -1,
                    webkitAnimationDelay: -1,
                    MozAnimationDelay: -1
                },
                scaleY: "{0%,40%,100%{-moz-transform:scaleY(0.2);-webkit-transform:scaleY(0.2);transform:scaleY(0.2);}20%,60%{-moz-transform:scaleY(1);-webkit-transform:scaleY(1);transform:scaleY(1);}}"
            };
            i(),
            this.appendto = function(t, e) {
                a = t,
                s = e,
                a.appendChild(r)
            }
            ,
            this.setPosition = function() {
                a && a.offsetHeight > 0 ? (r.style.top = (a.offsetHeight - b(l.ctn.height)) / 2 + "px",
                r.style.left = (a.offsetWidth - b(l.ctn.width)) / 2 + "px") : s && s.DIMENSION.h_t && (r.style.top = (s.DIMENSION.h_t - b(l.ctn.height)) / 2 + "px",
                r.style.left = (s.DIMENSION._w - b(l.ctn.width)) / 2 + "px")
            }
            ,
            this.show = function() {
                n(),
                r.style.display = ""
            }
            ,
            this.hide = function() {
                clearTimeout(o),
                r.style.display = "none"
            }
        }
        function s(t) {
            t = t || {};
            var e, i, n, r, a, o, s = u.$C("div"), l = 70, c = function() {
                clearTimeout(o),
                i && (i.style.display = "none",
                s.innerHTML = ""),
                e && f(e.closeCb) && e.closeCb()
            }, d = function(d) {
                if (e = d,
                clearTimeout(o),
                !i) {
                    i = u.$C("div"),
                    i.style.width = "100%",
                    i.style.height = "100%",
                    i.style.position = "absolute",
                    i.style.zIndex = l,
                    i.style.top = 0,
                    i.style.textAlign = "center",
                    n = u.$C("div"),
                    r = u.$C("div"),
                    a = u.$C("span"),
                    s.style.fontSize = "12px",
                    s.style.margin = "9px auto",
                    n.style.position = "absolute",
                    n.style.top = 0,
                    n.style.left = 0,
                    n.style.width = "100%",
                    n.style.height = "100%",
                    n.style.backgroundColor = t.TIP_ARR ? t.TIP_ARR[2] || "#fff" : "#fff",
                    n.style.opacity = .5,
                    n.style.filter = "alpha(opacity=50)",
                    r.style.padding = "1px 3px 10px",
                    r.style.top = t.TIP_ARR ? t.TIP_ARR[4] || "26%" : "26%",
                    r.style.position = "relative",
                    r.style.margin = "0 auto",
                    r.style.width = "100%",
                    a.style.cursor = "pointer",
                    a.style.display = "block",
                    a.style.margin = "0 auto",
                    a.style.lineHeight = a.style.height = "28px",
                    a.style.width = "60px",
                    a.style.fontSize = "14px",
                    a.style.borderRadius = "3px",
                    u.xh5_EvtUtil.addHandler(a, "click", c),
                    r.appendChild(s);
                    var h = !(!t.TIP_ARR || !t.TIP_ARR[3]);
                    !h && i.appendChild(n),
                    i.appendChild(r)
                }
                i.style.display = "",
                s.style.color = "undefined" != typeof d.fontColor ? d.fontColor : t.TIP_ARR ? t.TIP_ARR[1] || "#fff" : "#fff";
                var f = t.TIP_ARR ? t.TIP_ARR[0] || "#000" : "#000";
                if (r.style.backgroundColor = u.xh5_BrowserUtil.noH5 ? f : u.hex2dec(f, .8),
                d.bgStyle)
                    for (var m in d.bgStyle)
                        d.bgStyle.hasOwnProperty(m) && (r.style[m] = d.bgStyle[m]);
                if (s.innerHTML = d.txt || "",
                d.content && s.appendChild(d.content),
                !isNaN(d.autoHide) && d.autoHide > 0 && setTimeout(c, 1e3 * d.autoHide),
                d.noBtn ? u.$CONTAINS(r, a) && r.removeChild(a) : (a.innerHTML = d.btnLb || "\u786e\u5b9a",
                a.style.background = t.BTN_ARR ? t.BTN_ARR[0] || "#2b9dfc" : "#2b9dfc",
                a.style.color = t.BTN_ARR ? t.BTN_ARR[1] || "#fff" : "#fff",
                !u.$CONTAINS(r, a) && r.appendChild(a)),
                d.extraBtn)
                    for (var p = 0, g = d.extraBtn, v = g.length; v > p; p++) {
                        var b = g[p]
                          , N = u.$C("input");
                        N.type = "button",
                        N.value = b.value,
                        N.style.marginTop = "20px",
                        N.style.cursor = "pointer",
                        u.xh5_EvtUtil.addHandler(N, "click", b.onClk),
                        r.appendChild(N)
                    }
                return d.parent.appendChild(i),
                i
            };
            this.genTip = d,
            this.hide = c
        }
        function l() {
            var t = "hq";
            return location.hostname.indexOf("sina.cn") > -1 && (t = "w",
            location.pathname.indexOf("appchart") > -1 && (t = "a")),
            t
        }
        this.VER = "2.5.2";
        var u = this
          , c = function(t) {
            return function(e) {
                return {}.toString.call(e) == "[object " + t + "]"
            }
        }
          , d = c("Object")
          , h = c("String")
          , f = c("Function")
          , m = c("Array")
          , p = c("Number")
          , g = c("Date");
        this.isObj = d,
        this.isStr = h,
        this.isFunc = f,
        this.isArr = m,
        this.isNum = p,
        this.isDate = g;
        var v = {
            LSE: [["8:00", "16:30"]],
            US: [["9:30", "16:00"]],
            HK: [["09:30", "11:59"], ["13:00", "16:00"]],
            HKAP: [["16:15", "18:30"]],
            CN_b: [["9:30", "11:30"], ["13:01", "15:00"]],
            REPO_b: [["9:30", "11:30"], ["13:01", "15:30"]],
            CN: [["9:30", "11:30"], ["13:01", "15:00"]],
            fund: [["9:30", "11:30"], ["13:01", "15:00"]],
            OTC: [["9:30", "11:30"], ["13:01", "15:00"]],
            REPO: [["9:30", "11:30"], ["13:01", "15:30"]],
            GOODS: [["20:00", "23:59"], ["00:00", "02:29"], ["09:00", "15:30"]],
            MSCI: [["07:00", "23:59"], ["00:00", "06:00"]],
            option_cn: [["9:30", "11:30"], ["13:01", "15:00"]],
            globalbd: [["08:00", "23:59"], ["00:00", "07:59"]]
        }
          , b = function(t) {
            return parseInt(t, 10)
        };
        this.uae = function(t) {
            for (var e, i = [], n = {}, r = 0, a = t.length; a > r; r++)
                e = t[r],
                1 !== n[e] && (n[e] = 1,
                i[i.length] = e);
            return i
        }
        ;
        var N = new function() {
            var t;
            if (XMLHttpRequest)
                t = new XMLHttpRequest;
            else if (ActiveXObject)
                try {
                    t = new ActiveXObject("MSXML2.XMLHTTP")
                } catch (e) {
                    try {
                        t = new ActiveXObject("Microsoft.XMLHTTP")
                    } catch (i) {}
                }
            this.send = function(e, i, n, r) {
                if (!t || !e)
                    return void (n && n("error while sending"));
                if (e += e.indexOf("?") < 0 ? "?" : "&",
                e += "_=" + (new Date).getTime(),
                r = r || "POST",
                t.onreadystatechange = function() {
                    if (4 == t.readyState) {
                        var e;
                        200 == t.status && (e = t.responseText),
                        n && n(e)
                    }
                }
                ,
                t.open(r, e, !0),
                "POST" == r) {
                    t.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;");
                    var a = "";
                    for (var o in i)
                        i.hasOwnProperty(o) && (a += [encodeURIComponent(o), encodeURIComponent(i[o])].join("=") + "&");
                    t.send(a)
                } else
                    t.send(null)
            }
        }
        ;
        this.POST = "undefined" != typeof jQuery && jQuery.post ? jQuery.post : N.send,
        this.trace = function(t) {
            return {
                log: function() {
                    t && t.log && t.log.apply(t, arguments)
                },
                error: function() {
                    t && t.error && t.error.apply(t, arguments)
                }
            }
        }(null);
        var y = function(t, e) {
            var i = -1;
            if (t.indexOf)
                i = t.indexOf(e);
            else
                for (var n = t.length; n--; )
                    if (t[n] === e) {
                        i = n;
                        break
                    }
            return i
        };
        this.arrIndexOf = y;
        var w = function(t, e) {
            if (null == t || "object" != typeof t)
                return t;
            if (t.constructor == Date || t.constructor == RegExp || f(t) || h(t) || t.constructor == Number || t.constructor == Boolean)
                return new t.constructor(t);
            e = e || new t.constructor;
            for (var i in t)
                t.hasOwnProperty(i) && (e[i] = "undefined" == typeof e[i] ? w(t[i], null) : e[i]);
            return e
        };
        this.clone = w;
        var x = function(t) {
            if (!t)
                return t;
            var e = {};
            for (var i in t)
                t.hasOwnProperty(i) && (e[i] = t[i]);
            return e
        };
        this.co = x;
        var S = this;
        this.oc = function(t, e) {
            if (!t)
                return e;
            for (var i in e)
                e.hasOwnProperty(i) && (t[i] = d(t[i]) && d(e[i]) ? S.oc(t[i], e[i]) : e[i]);
            return t
        }
        ;
        var k = function(t) {
            function e() {}
            return e.prototype = t,
            new e
        };
        this.fInherit = t,
        this.urlUtil = new function() {
            this.getUrlParam = function() {
                var t, e = {};
                try {
                    t = location.search.substring(1)
                } catch (i) {}
                if (t)
                    for (var n, r, a, o = t.split("&"), s = o.length, l = 0; s > l; l++)
                        a = o[l].indexOf("="),
                        -1 != a && (n = o[l].substring(0, a),
                        r = o[l].substring(a + 1),
                        e[n] = r);
                return e
            }
            ,
            this.getMainUrl = function() {
                return window.location != window.parent.location ? document.referrer : document.location.href
            }
        }
        ,
        this.xh5_BrowserUtil = new function() {
            this.info = function() {
                var t, e = navigator.userAgent, i = e.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];
                return /trident/i.test(i[1]) ? (t = /\brv[ :]+(\d+)/g.exec(e) || [],
                {
                    name: "IE ",
                    version: t[1] || ""
                }) : "Chrome" === i[1] && (t = e.match(/\bOPR\/(\d+)/),
                null != t) ? {
                    name: "Opera",
                    version: t[1]
                } : (i = i[2] ? [i[1], i[2]] : [navigator.appName, navigator.appVersion, "-?"],
                null != (t = e.match(/version\/(\d+)/i)) && i.splice(1, 1, t[1]),
                {
                    name: i[0],
                    version: i[1]
                })
            }(),
            this.noH5 = !1,
            this.hdpr = function(t) {
                var e = document.createElement("canvas");
                if (e.getContext && e.getContext("2d")) {
                    var i = Math.ceil(window.devicePixelRatio || 1)
                      , n = e.getContext("2d").webkitBackingStorePixelRatio || 1;
                    return i / n
                }
                return t.noH5 = !0,
                1
            }(this)
        }
        ,
        this.xh5_deviceUtil = function() {
            return {
                istd: function() {
                    if ("ontouchend"in window) {
                        var t;
                        try {
                            t = navigator.userAgent
                        } catch (e) {}
                        return t && t.indexOf("Windows NT") > 0 ? !1 : !0
                    }
                    return !1
                }(),
                allowt: "ontouchend"in window
            }
        }();
        var T = function() {
            function t(t) {
                return t = JSON.stringify(t),
                t || (t = ""),
                t = encodeURIComponent(t)
            }
            function e(t) {
                try {
                    t = JSON.parse(t)
                } catch (e) {
                    t = decodeURIComponent(t)
                }
                return t
            }
            function i(e, i, n) {
                if (n = n || {},
                void 0 != e && void 0 != i) {
                    var r, a, o, s;
                    a = n.path ? "; path=" + n.path : "",
                    o = n.domain ? "; domain=" + n.domain : "",
                    s = n.secure ? "; secure" : "";
                    var l, c = n.expires;
                    switch (u(c)) {
                    case "Number":
                        l = new Date,
                        l.setTime(l.getTime() + 1e3 * c);
                        break;
                    case "String":
                        l = new Date(c),
                        "Invalid Date" == l && (l = "");
                        break;
                    case "Date":
                        l = c
                    }
                    r = l ? "; expires=" + l.toUTCString() : "",
                    document.cookie = [encodeURIComponent(e), "=", t(i), r, a, o, s].join("")
                }
            }
            function n(t) {
                var i = document.cookie.match("(?:^|;)\\s*" + encodeURIComponent(t) + "=([^;]*)");
                return i ? e(i[1]) || "" : null
            }
            function r(t) {
                document.cookie = encodeURIComponent(t) + "=;expires=" + new Date(0).toUTCString()
            }
            function a(e, i) {
                void 0 != e && void 0 != i && localStorage.setItem(encodeURIComponent(e), t(i))
            }
            function o(t) {
                var i = localStorage.getItem(encodeURIComponent(t));
                return e(i)
            }
            function s(t) {
                localStorage.removeItem(encodeURIComponent(t))
            }
            var l = Object.prototype.toString
              , u = function(t) {
                return null === t ? "Null" : void 0 === t ? "Undefined" : l.call(t).slice(8, -1)
            }
              , c = function() {
                if ("object" == typeof localStorage && localStorage && localStorage.setItem) {
                    var t = "KKE_LOCALSTORAGE_TESTing";
                    try {
                        return localStorage.removeItem(t),
                        localStorage.setItem(t, t),
                        localStorage.removeItem(t),
                        !0
                    } catch (e) {
                        return !1
                    }
                }
                return !1
            }();
            return {
                hasls: c,
                save: function(t, e, n) {
                    n = n || {};
                    var r = n.mode;
                    if (r)
                        switch (r) {
                        case "localStorage":
                            if (!c)
                                return;
                            a(t, e);
                            break;
                        case "cookie":
                            i(t, e, n)
                        }
                    else if (c)
                        try {
                            s(t),
                            a(t, e)
                        } catch (o) {}
                    else
                        i(t, e, n)
                },
                load: function(t, e) {
                    var i;
                    if ("Object" == u(e) && (e = e.mode),
                    e)
                        switch (e) {
                        case "localStorage":
                            if (!c)
                                return;
                            i = o(t);
                            break;
                        case "cookie":
                            i = n(t)
                        }
                    else
                        c && (i = o(t)),
                        !i && (i = n(t));
                    return i
                },
                remove: function(t, e) {
                    if ("Object" == u(e) && (e = e.mode),
                    e)
                        switch (e) {
                        case "localStorage":
                            if (!c)
                                return;
                            s(t);
                            break;
                        case "cookie":
                            r(t)
                        }
                    else
                        c && s(t),
                        r(t)
                },
                clear: function(t) {
                    c && s(t)
                }
            }
        }();
        this.localSL = T,
        this.xh5_EvtUtil = {
            addHandler: function(t, e, i) {
                t && (t.addEventListener ? t.addEventListener(e, i, !1) : t.attachEvent ? t.attachEvent("on" + e, i) : t["on" + e] = i)
            },
            removeHandler: function(t, e, i) {
                t && (t.removeEventListener ? t.removeEventListener(e, i, !1) : t.detachEvent ? t.detachEvent("on" + e, i) : t["on" + e] = null)
            },
            getEvent: function(t) {
                return t ? t : window.event
            },
            getTarget: function(t) {
                return !t && (t = this.getEvent()),
                t ? t.target || t.srcElement : null
            },
            preventDefault: function(t) {
                !t && (t = this.getEvent()),
                t && (t.preventDefault ? t.preventDefault() : t.returnValue = !1)
            },
            stopPropagation: function(t) {
                !t && (t = this.getEvent()),
                t && (t.stopPropagation ? t.stopPropagation() : t.cancelBubble = !0)
            },
            getRelatedTarget: function(t) {
                return !t && (t = this.getEvent()),
                t.relatedTarget ? t.relatedTarget : t.toElement ? t.toElement : t.fromElement ? t.fromElement : null
            },
            getWheelDelta: function(t) {
                return !t && (t = this.getEvent()),
                t ? t.wheelDelta ? client.engine.opera && client.engine.opera < 9.5 ? -t.wheelDelta : t.wheelDelta : 40 * -t.detail : 0
            }
        },
        e.prototype.al = function(t, e, i) {
            i && this.evtObj[t] || (!this.evtObj[t] && (this.evtObj[t] = []),
            this.evtObj[t].push(e))
        }
        ,
        e.prototype.rl = function(t, e) {
            var i = this.evtObj[t];
            if (m(i))
                for (var n = i.length; n--; )
                    i[n] == e && i.splice(n, 1)
        }
        ,
        e.prototype.re = function(t, e) {
            var i = this.evtObj[t];
            if (m(i))
                for (var n = 0, r = i.length; r > n; n++)
                    "function" == typeof i[n] && i[n](t, e)
        }
        ,
        this.xh5_EvtDispatcher = e,
        this.$DOM = function(t, e) {
            return e = e || document,
            e.getElementById(t)
        }
        ,
        this.$C = function(t, e) {
            var i = document.createElement(t);
            return e && (i.id = e),
            i
        }
        ,
        this.$T = function(t) {
            return document.createTextNode(t)
        }
        ,
        this.$CONTAINS = function(t, e) {
            if (t.compareDocumentPosition)
                return t === e || !!(16 & t.compareDocumentPosition(e));
            if (t.contains && 1 === e.nodeType)
                return t.contains(e) && t !== e;
            for (; e = e.parentNode; )
                if (e === t)
                    return !0;
            return !1
        }
        ,
        this.getTextNodes = function(t) {
            var e = [];
            for (t = t.firstChild; t; t = t.nextSibling)
                3 == t.nodeType ? e.push(t) : e = e.concat(arguments.callee(t));
            return e
        }
        ,
        this.getCSS = function(t) {
            var e = null;
            return e = window.getComputedStyle ? window.getComputedStyle(t) : t.currentStyle
        }
        ,
        this.fBind = i,
        this.isColor = function(t) {
            return /^#[0-9a-fA-F]{3,6}$/.test(t)
        }
        ,
        this.isColorRGB = function(t) {
            return /(^#[0-9a-fA-F]{3,6}$)|(^rgba?\(.{5,16}\)$)/.test(t)
        }
        ,
        this.randomColor = function() {
            for (var t = Math.floor(16777215 * Math.random()).toString(16); t.length < 6; )
                t += "0";
            return t
        }
        ,
        this.hex2dec = function(t, e, i) {
            if (0 == t.indexOf("rgb"))
                return t;
            t = t.replace(/#|0x/i, "");
            var n, r, a;
            t.replace(/(\w{6})|(\w{3})/, function(e, i, o) {
                if (i)
                    n = t.slice(0, 2),
                    r = t.slice(2, 4),
                    a = t.slice(4);
                else {
                    if (!o)
                        return [0, 0, 0];
                    var s = t.split("");
                    n = s[0],
                    n += String(n),
                    r = s[1],
                    r += String(r),
                    a = s[2],
                    a += String(a)
                }
            });
            var o;
            return isNaN(e) ? (o = [parseInt(n, 16), parseInt(r, 16), parseInt(a, 16)],
            i ? o : "rgb($color)".replace("$color", o.join(","))) : (o = [parseInt(n, 16), parseInt(r, 16), parseInt(a, 16), e],
            i ? o : "rgba($color)".replace("$color", o.join(",")))
        }
        ,
        this.getTimestamp = n,
        this.cssUtil = {
            inject: function(t) {
                var e = document.createElement("style")
                  , i = document.head || document.getElementsByTagName("head")[0] || document.documentElement;
                e.type = "text/css",
                e.styleSheet ? e.styleSheet.cssText = t : e.appendChild(document.createTextNode(t)),
                i.appendChild(e)
            },
            adCls: function(t, e) {
                if (t.className != e) {
                    var i = t.className.split(" ");
                    for (var n in i)
                        if (i.hasOwnProperty(n) && i[n] == e)
                            return;
                    "" == t.className ? t.className = e : t.className += " " + e
                }
            },
            rmCls: function(t, e) {
                if (-1 != t.className.indexOf(e))
                    if (t.className == e)
                        t.className = "";
                    else {
                        var i = t.className.split(" ")
                          , n = "";
                        for (var r in i)
                            if (i.hasOwnProperty(r)) {
                                if (i[r] == e)
                                    continue;
                                "" != n && (n += " "),
                                n += i[r]
                            }
                        t.className = n
                    }
            }
        },
        this.load = a;
        var P, C = new function() {
            var t = P || {};
            P = t;
            var e = function(e, i) {
                for (var n = t[e][i ? "errCbArr" : "cbArr"], r = n.length; r--; ) {
                    var a = n[r];
                    f(a) && a()
                }
                t[e] = null,
                delete t[e]
            };
            this.load = function(n, o, s, l) {
                var u = "urlhash_" + r(n);
                for (var c in t)
                    if (t.hasOwnProperty(c) && c == u)
                        return t[c].cbArr.push(o),
                        void t[c].errCbArr.push(s);
                t[u] = {
                    url: n,
                    cbArr: [o],
                    errCbArr: [s]
                },
                a(n, i(e, this, u), i(e, this, u, !0), l)
            }
        }
        ;
        this.relyLoader = C,
        this.iframer = function(t, e) {
            function i() {
                if (document && document.body) {
                    clearInterval(r),
                    o = 0;
                    var t = document.body;
                    t.insertBefore(n, t.firstChild),
                    n.setAttribute("data-ready", "1")
                } else
                    o++ > 9 && (clearInterval(r),
                    f(e) && e())
            }
            var n, r, a = t.attribute ? t.attribute.id || "_kkeiframe" + (new Date).getTime() : "_kkeiframe" + (new Date).getTime(), o = 0;
            if (!(n = document.getElementById(a))) {
                if (n = document.createElement("iframe"),
                n.setAttribute("data-ready", "0"),
                t.attribute)
                    for (var s in t.attribute)
                        t.attribute.hasOwnProperty(s) && (n[s] = t.attribute[s]);
                if (n.style.height = n.style.width = 0,
                n.style.borderStyle = "none",
                n.style.position = "absolute",
                n.style.zIndex = -9,
                n.style.display = "none",
                t.style)
                    for (var l in t.style)
                        t.style.hasOwnProperty(l) && (n.style[l] = t.style[l]);
                r = setInterval(i, 500),
                i()
            }
            return n
        }
        ,
        this.ca = function(t) {
            if (t)
                for (; t.length > 0; )
                    t.length--
        }
        ,
        this.isLongtime = function(t) {
            return ["sz399289", "sz399290", "sz399298", "sz399299", "sz399302", "sz399301", "sz399481", "sh000012", "sh000022", "sh000061", "sh000101", "sh000116", "sh000923"].indexOf(t) > -1
        }
        ,
        this.isRepos = function(t) {
            return /^(sh204\d{3}|sz1318\d{2})$/.test(t)
        }
        ,
        this.isCNK = function(t) {
            return /^(sh688\d{3}|sh689\d{3})$/.test(t) ? "CNK" : void 0
        }
        ,
        this.market = function(t) {
            return /^(sh204\d{3}|sz1318\d{2})$/.test(t) ? "REPO" : /^si\w+$/.test(t) ? "SI" : /^s[hz]\d{6}$/.test(t) ? "CN" : /^bj\w+/.test(t) ? "CN" : /^GN|gn\d{7}$/.test(t) ? "CN" : /^HY|hy\d{7}$/.test(t) ? "CN" : /^DY|dy\d{7}$/.test(t) ? "CN" : /^s[hz]\d{6}_i$/.test(t) ? "CNI" : /^sb[48]\d{5}$/.test(t) ? "OTC" : /^[48]\d{5}$/.test(t) ? "OTC" : /^otc_\d{6}$/.test(t) ? "OTC" : /^btc_\w+/.test(t) ? "BTC" : /^gb_.+$/.test(t) ? "US" : /^(hk|rt_hk)\w+_preipo$/.test(t) ? "HKAP" : /^(hk|rt_hk)\w+/.test(t) ? "HK" : /^hf_\w+/.test(t) ? "HF" : /^globalbd_.+$/.test(t) ? "globalbd" : /^lse_.+$/.test(t) ? "LSE" : /^nf_\w+/.test(t) ? "NF" : /^gds_\w+/.test(t) ? "GOODS" : /^f_\d{6}$/.test(t) || /^fu_\d{6}$/.test(t) || /^pwbfbyd_\d{6}$/.test(t) || /^pwbfbjd_\d{6}$/.test(t) || /^pwbfbnd_\d{6}$/.test(t) || /^ljjz_\d{6}$/.test(t) || /^dwjz_\d{6}$/.test(t) || /^lshb_\d{6}$/.test(t) ? "fund" : /^CON_OP_\w+/.test(t) ? "option_cn" : /^P_OP_\w+/.test(t) ? "op_m" : /^znb_\w+/.test(t) ? "global_index" : /^fx_.+$/.test(t) ? "forex" : /^(DINIW|USDCNY)$/.test(t) ? "forex_yt" : /^CFF_RE_.+$/.test(t) ? "CFF" : /^msci_\w+/.test(t) ? "MSCI" : /\d+$/.test(t) ? "NF" : void 0
        }
        ,
        this.cookieUtil = {
            escape: function(t) {
                return t.replace(/([.*+?^${}()|[\]\/\\])/g, "\\$1")
            },
            get: function(t) {
                var e = document.cookie.match("(?:^|;)\\s*" + this.escape(t) + "=([^;]*)");
                return e ? e[1] || "" : ""
            },
            set: function(t, e, i) {
                !i && (i = {}),
                e || (e = "",
                i.expires = -1);
                var n = "";
                if (i.expires && (Number(i.expires) || i.expires.toUTCString)) {
                    var r;
                    Number(i.expires) ? (r = new Date,
                    r.setTime(r.getTime() + 1e3 * i.expires)) : r = i.expires,
                    n = "; expires=" + r.toUTCString()
                }
                var a = i.path ? "; path=" + i.path : ""
                  , o = i.domain ? "; domain=" + i.domain : ""
                  , s = i.secure ? "; secure" : "";
                document.cookie = [t, "=", e, n, a, o, s].join("")
            }
        };
        var _ = new function() {
            function t(e) {
                a(e.url, function() {
                    for (var t = e.f(); t && e.q.length; ) {
                        var i = e.q.shift();
                        t.apply(null, i)
                    }
                }, function() {
                    --e.count && t(e),
                    e.count < 1 && (e.q = [])
                })
            }
            function e(e) {
                setTimeout(function() {
                    var i = !!e.f();
                    !i && t(e)
                }, 2e3)
            }
            function i(t) {
                if ("undefined" != typeof SIMA) {
                    for (var e, i = s.length; i--; )
                        if (e = s[i],
                        e.symbol == t.symbol && e.type == t.type)
                            return;
                    s.push(t)
                }
                var n = t.simadata
                  , r = {
                    action: "hq",
                    data: n,
                    pk: "179824"
                };
                try {
                    SIMA(r)
                } catch (a) {
                    o.count && o.q.push([t])
                }
            }
            var n = navigator.userAgent || "unknownUa";
            n = encodeURIComponent("_UA_" + n);
            var r = {
                url: "//mjs.sinaimg.cn/umd/base-tools-SUDA/1.0.2/index.all.min.js",
                q: [],
                count: 5,
                f: function() {
                    return "undefined" == typeof SUDA ? void 0 : SUDA.uaTrack
                }
            }
              , o = {
                url: "//news.sina.com.cn/js/pctianyi/sima.js",
                q: [],
                count: 5,
                f: function() {
                    return "undefined" == typeof SIMA ? void 0 : i
                }
            };
            e(o),
            e(r);
            var s = [];
            this.sima = i;
            var l, u, c = [], d = function() {
                for (var t, e = "chart_finance", i = "", a = ",", o = "", s = 0, u = c.length; u > s; s++)
                    t = c[s],
                    o += [t.k, t.v].join(i) + a;
                for (; c.length; )
                    c.length--;
                if (o !== l) {
                    l = o,
                    o += n;
                    try {
                        SUDA.uaTrack(e, o)
                    } catch (d) {
                        r.count && r.q.push([e, o])
                    }
                }
            };
            this.s = function(t, e, i) {
                if (t) {
                    (isNaN(i) || 0 > i) && (i = 3e3),
                    e = JSON.stringify(e),
                    e || (e = ""),
                    e = encodeURIComponent(e);
                    for (var n = c.length; n--; )
                        if (c[n].k == t) {
                            c.splice(n, 1);
                            break
                        }
                    c.push({
                        k: t,
                        v: e
                    }),
                    clearTimeout(u),
                    u = setTimeout(d, i)
                }
            }
            ;
            var h, f;
            this.s2 = function(t, e, i) {
                if (i = i || "chart_detail",
                f != t || h != i) {
                    h = i,
                    f = t,
                    setTimeout(function() {
                        h = void 0,
                        f = void 0
                    }, 99);
                    try {
                        SUDA.uaTrack(i, e || t)
                    } catch (n) {
                        r.count && r.q.push([i, e || t])
                    }
                }
            }
            ,
            this.log = function() {
                try {
                    SUDA.log()
                } catch (t) {}
            }
        }
        ;
        this.sudaLog = _.log,
        this.stc = _.s,
        this.suda = _.s2,
        this.xh5_PosUtil = {
            pp: function(t, e, i, n) {
                return isNaN(t) || e >= t ? n : t >= i ? 1 : Math.max(n * (1 - (t - e) / (i - e)), 1)
            },
            ppp: function(t, e, i, n, r) {
                return t = (t - r) / r,
                this.pp(t, e, i, n)
            },
            vp: function(t, e, i) {
                return isNaN(t) || 0 >= t ? i - 1 : i * (1 - t / e)
            }
        },
        this.xh5_HtmlPosUtil = {
            pageX: function(t) {
                return t.offsetParent ? t.offsetLeft + this.pageX(t.offsetParent) : t.offsetLeft
            },
            pageY: function(t) {
                return t.offsetParent ? t.offsetTop + this.pageY(t.offsetParent) : t.offsetTop
            },
            parentX: function(t) {
                return t.parentNode == t.offsetParent ? t.offsetLeft : this.pageX(t) - this.pageX(t.parentNode)
            },
            parentY: function(t) {
                return t.parentNode == t.offsetParent ? t.offsetTop : this.pageY(t) - this.pageY(t.parentNode)
            }
        },
        this.xh5_ADJUST_HIGH_LOW = new function() {
            var t = function(t) {
                var e = parseInt(Math.round(100 * t));
                return e % 100 != 0 && (e % 10 == 0 && (e *= .1),
                e % 5 != 0 && e % 2 != 0) ? !0 : !1
            }
              , e = function(t, e) {
                if (e)
                    for (; t > 5; )
                        if (t % 2 == 0)
                            t *= .5;
                        else {
                            if (t % 3 != 0)
                                break;
                            t /= 3
                        }
                else
                    t > 9 && (t % 3 == 0 ? t /= 3 : t % 4 == 0 ? t *= .25 : t % 2 == 0 && (t *= .5));
                return t
            };
            this.c = function(i, n, r, a, o, s) {
                if (isNaN(i) || isNaN(n) || n > i)
                    return [0, 0, 0];
                isNaN(s) || (s = (i - n) * s,
                i += s,
                n -= s);
                for (var l, u, c, d, h, f, m, p, g, v, b, N, y, w, x = -1e-6, S = .5 * (n + i), k = a ? [4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20] : [4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20], T = [1, 2, 3, 4, 5, 6, 8], P = !1, C = T.length, _ = 0, D = k.length; D > _; _++)
                    for (P = !1,
                    y = k[_],
                    c = (i - n) / y,
                    p = Math.pow(10, 0 - r); !P; ) {
                        for (w = 0; C > w; w++)
                            if (d = p * T[w],
                            d - c > x && (1 & y ? (h = Math.round((S + .5 * d) / d) * d,
                            b = (h + .5 * (y - 1) * d).toFixed(5),
                            N = (h - .5 * (y + 1) * d).toFixed(5)) : (h = Math.round(S / d) * d,
                            b = (h + .5 * y * d).toFixed(5),
                            N = (h - .5 * y * d).toFixed(5)),
                            f = Number(b),
                            m = Number(N),
                            f - i > x && x > m - n)) {
                                if (P = !0,
                                0 > m && !o && (f -= m,
                                m = 0),
                                !g) {
                                    g = f - m,
                                    l = f,
                                    u = m,
                                    v = y;
                                    break
                                }
                                var R = (f - m) / e(y);
                                if (1 != Math.round(100 * R) && 1 != Math.round(10 * R) && t(R))
                                    break;
                                if (f - m > g)
                                    break;
                                if (f - m == g) {
                                    var A = l - i
                                      , O = n - u
                                      , E = Math.abs(A - O);
                                    A = f - i,
                                    O = n - m;
                                    var I = Math.abs(A - O);
                                    if (I >= E)
                                        break
                                }
                                if (t(f))
                                    break;
                                if (t(m))
                                    break;
                                g = f - m,
                                l = f,
                                u = m,
                                v = y;
                                break
                            }
                        p *= 10
                    }
                return v = e(v, a),
                [l, u, v]
            }
        }
        ,
        this.xh5_S_KLC_D = function(t) {
            var e, i, n, r, a, o, s, l = (arguments,
            864e5), u = 7657, c = [], d = [], h = ~(3 << 30), f = 1 << 30, m = [0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29, 30], p = Math, g = function() {
                var l, u;
                for (l = 0; 64 > l; l++)
                    d[l] = p.pow(2, l),
                    26 > l && (c[l] = v(l + 65),
                    c[l + 26] = v(l + 97),
                    10 > l && (c[l + 52] = v(l + 48)));
                for (c.push("+", "/"),
                c = c.join(""),
                i = t.split(""),
                n = i.length,
                l = 0; n > l; l++)
                    i[l] = c.indexOf(i[l]);
                return r = {},
                e = o = 0,
                a = {},
                u = w([12, 6]),
                s = 63 ^ u[1],
                {
                    _1479: D,
                    _136: _,
                    _200: C,
                    _139: R,
                    _197: A,
                    _3466: O
                }["_" + u[0]] || function() {
                    return []
                }
            }, v = String.fromCharCode, b = function(t) {
                return t === {}._
            }, N = function() {
                var t, e;
                for (t = y(),
                e = 1; ; ) {
                    if (!y())
                        return e * (2 * t - 1);
                    e++
                }
            }, y = function() {
                var t;
                return e >= n ? 0 : (t = i[e] & 1 << o,
                o++,
                o >= 6 && (o -= 6,
                e++),
                !!t)
            }, w = function(t, r, a) {
                var s, l, u, c, h;
                for (l = [],
                u = 0,
                r || (r = []),
                a || (a = []),
                s = 0; s < t.length; s++)
                    if (c = t[s],
                    u = 0,
                    c) {
                        if (e >= n)
                            return l;
                        if (t[s] <= 0)
                            u = 0;
                        else if (t[s] <= 30) {
                            for (; h = 6 - o,
                            h = c > h ? h : c,
                            u |= (i[e] >> o & (1 << h) - 1) << t[s] - c,
                            o += h,
                            o >= 6 && (o -= 6,
                            e++),
                            c -= h,
                            !(0 >= c); )
                                ;
                            r[s] && u >= d[t[s] - 1] && (u -= d[t[s]])
                        } else
                            u = w([30, t[s] - 30], [0, r[s]]),
                            a[s] || (u = u[0] + u[1] * d[30]);
                        l[s] = u
                    } else
                        l[s] = 0;
                return l
            }, x = function() {
                var t;
                return t = w([3])[0],
                1 == t ? (r.d = w([18], [1])[0],
                t = 0) : t || (t = w([6])[0]),
                t
            }, S = function(t) {
                var e, i, n;
                for (t > 1 && (e = 0),
                e = 0; t > e; e++)
                    r.d++,
                    n = r.d % 7,
                    (3 == n || 4 == n) && (r.d += 5 - n);
                return i = new Date,
                i.setTime((u + r.d) * l),
                i
            }, k = function(t) {
                var e, i, n;
                for (n = r.wd || 62,
                e = 0; t > e; e++)
                    do
                        r.d++;
                    while (!(n & 1 << (r.d % 7 + 10) % 7));
                return i = new Date,
                i.setTime((u + r.d) * l),
                i
            }, T = function(t) {
                var e, i, n;
                return t ? 0 > t ? (e = T(-t),
                [-e[0], -e[1]]) : (e = t % 3,
                i = (t - e) / 3,
                n = [i, i],
                e && n[e - 1]++,
                n) : [0, 0]
            }, P = function(t, e, i) {
                var n, r, a;
                for (r = "number" == typeof e ? T(e) : e,
                a = T(i),
                n = [a[0] - r[0], a[1] - r[1]],
                r = 1; n[0] < n[1]; )
                    r *= 5,
                    n[1]--;
                for (; n[1] < n[0]; )
                    r *= 2,
                    n[0]--;
                if (r > 1 && (t *= r),
                n = n[0],
                t = E(t),
                0 > n) {
                    for (; t.length + n <= 0; )
                        t = "0" + t;
                    return n += t.length,
                    r = t.substr(0, n) - 0,
                    void 0 === i ? r + "." + t.substr(n) - 0 : (a = t.charAt(n) - 0,
                    a > 5 ? r++ : 5 == a && (t.substr(n + 1) - 0 > 0 ? r++ : r += 1 & r),
                    r)
                }
                for (; n > 0; n--)
                    t += "0";
                return t - 0
            }, C = function() {
                var t, i, a, o, l;
                if (s >= 1)
                    return [];
                for (r.d = w([18], [1])[0] - 1,
                a = w([3, 3, 30, 6]),
                r.p = a[0],
                r.ld = a[1],
                r.cd = a[2],
                r.c = a[3],
                r.m = p.pow(10, r.p),
                r.pc = r.cd / r.m,
                i = [],
                t = 0; o = {
                    d: 1
                },
                y() && (a = w([3])[0],
                0 == a ? o.d = w([6])[0] : 1 == a ? (r.d = w([18])[0],
                o.d = 0) : o.d = a),
                l = {
                    date: S(o.d)
                },
                y() && (r.ld += N()),
                a = w([3 * r.ld], [1]),
                r.cd += a[0],
                l.close = r.cd / r.m,
                i.push(l),
                !(e >= n) && (e != n - 1 || 63 & (r.c ^ t + 1)); t++)
                    ;
                return i[0].prevclose = r.pc,
                i
            }, _ = function() {
                var t, i, a, o, l, u, c, d, h, f, m;
                if (s > 2)
                    return [];
                for (c = [],
                h = {
                    v: "volume",
                    p: "price",
                    a: "avg_price"
                },
                r.d = w([18], [1])[0] - 1,
                d = {
                    date: S(1)
                },
                a = w(1 > s ? [3, 3, 4, 1, 1, 1, 5] : [4, 4, 4, 1, 1, 1, 3]),
                t = 0; 7 > t; t++)
                    r[["la", "lp", "lv", "tv", "rv", "zv", "pp"][t]] = a[t];
                for (r.m = p.pow(10, r.pp),
                s >= 1 ? (a = w([3, 3]),
                r.c = a[0],
                a = a[1]) : (a = 5,
                r.c = 2),
                r.pc = w([6 * a])[0],
                d.pc = r.pc / r.m,
                r.cp = r.pc,
                r.da = 0,
                r.sa = r.sv = 0,
                t = 0; !(e >= n) && (e != n - 1 || 7 & (r.c ^ t)); t++) {
                    for (l = {},
                    o = {},
                    f = r.tv ? y() : 1,
                    i = 0; 3 > i; i++)
                        if (m = ["v", "p", "a"][i],
                        (f ? y() : 0) && (a = N(),
                        r["l" + m] += a),
                        u = "v" == m && r.rv ? y() : 1,
                        a = w([3 * r["l" + m] + ("v" == m ? 7 * u : 0)], [!!i])[0] * (u ? 1 : 100),
                        o[m] = a,
                        "v" == m) {
                            if (!(l[h[m]] = a) && (s > 1 || 241 > t) && (r.zv ? !y() : 1)) {
                                o.p = 0;
                                break
                            }
                        } else
                            "a" == m && (r.da = (1 > s ? 0 : r.da) + o.a);
                    r.sv += o.v,
                    l[h.p] = (r.cp += o.p) / r.m,
                    r.sa += o.v * r.cp,
                    l[h.a] = b(o.a) ? t ? c[t - 1][h.a] : l[h.p] : r.sv ? ((p.floor((r.sa * (2e3 / r.m) + r.sv) / r.sv) >> 1) + r.da) / 1e3 : l[h.p] + r.da / 1e3,
                    c.push(l)
                }
                return c[0].date = d.date,
                c[0].prevclose = d.pc,
                c
            }, D = function() {
                var t, e, i, n, a, o, l;
                if (s >= 1)
                    return [];
                for (r.lv = 0,
                r.ld = 0,
                r.cd = 0,
                r.cv = [0, 0],
                r.p = w([6])[0],
                r.d = w([18], [1])[0] - 1,
                r.m = p.pow(10, r.p),
                a = w([3, 3]),
                r.md = a[0],
                r.mv = a[1],
                t = []; a = w([6]),
                a.length; ) {
                    if (i = {
                        c: a[0]
                    },
                    n = {},
                    i.d = 1,
                    32 & i.c)
                        for (; ; ) {
                            if (a = w([6])[0],
                            63 == (16 | a)) {
                                l = 16 & a ? "x" : "u",
                                a = w([3, 3]),
                                i[l + "_d"] = a[0] + r.md,
                                i[l + "_v"] = a[1] + r.mv;
                                break
                            }
                            if (32 & a) {
                                o = 8 & a ? "d" : "v",
                                l = 16 & a ? "x" : "u",
                                i[l + "_" + o] = (7 & a) + r["m" + o];
                                break
                            }
                            if (o = 15 & a,
                            0 == o ? i.d = w([6])[0] : 1 == o ? (r.d = o = w([18])[0],
                            i.d = 0) : i.d = o,
                            !(16 & a))
                                break
                        }
                    n.date = S(i.d);
                    for (o in {
                        v: 0,
                        d: 0
                    })
                        b(i["x_" + o]) || (r["l" + o] = i["x_" + o]),
                        b(i["u_" + o]) && (i["u_" + o] = r["l" + o]);
                    for (i.l_l = [i.u_d, i.u_d, i.u_d, i.u_d, i.u_v],
                    l = m[15 & i.c],
                    1 & i.u_v && (l = 31 - l),
                    16 & i.c && (i.l_l[4] += 2),
                    e = 0; 5 > e; e++)
                        l & 1 << 4 - e && i.l_l[e]++,
                        i.l_l[e] *= 3;
                    i.d_v = w(i.l_l, [1, 0, 0, 1, 1], [0, 0, 0, 0, 1]),
                    o = r.cd + i.d_v[0],
                    n.open = o / r.m,
                    n.high = (o + i.d_v[1]) / r.m,
                    n.low = (o - i.d_v[2]) / r.m,
                    n.close = (o + i.d_v[3]) / r.m,
                    a = i.d_v[4],
                    "number" == typeof a && (a = [a, a >= 0 ? 0 : -1]),
                    r.cd = o + i.d_v[3],
                    l = r.cv[0] + a[0],
                    r.cv = [l & h, r.cv[1] + a[1] + !!((r.cv[0] & h) + (a[0] & h) & f)],
                    n.volume = (r.cv[0] & f - 1) + r.cv[1] * f,
                    t.push(n)
                }
                return t
            }, R = function() {
                var t, e, i, n;
                if (s > 1)
                    return [];
                for (r.l = 0,
                n = -1,
                r.d = w([18])[0] - 1,
                i = w([18])[0]; r.d < i; )
                    e = S(1),
                    0 >= n ? (y() && (r.l += N()),
                    n = w([3 * r.l], [0])[0] + 1,
                    t || (t = [e],
                    n--)) : t.push(e),
                    n--;
                return t
            }, A = function() {
                var t, i, a, o;
                if (s >= 1)
                    return [];
                for (r.f = w([6])[0],
                r.c = w([6])[0],
                a = [],
                r.dv = [],
                r.dl = [],
                t = 0; t < r.f; t++)
                    r.dv[t] = 0,
                    r.dl[t] = 0;
                for (t = 0; !(e >= n) && (e != n - 1 || 7 & (r.c ^ t)); t++) {
                    for (o = [],
                    i = 0; i < r.f; i++)
                        y() && (r.dl[i] += N()),
                        r.dv[i] += w([3 * r.dl[i]], [1])[0],
                        o[i] = r.dv[i];
                    a.push(o)
                }
                return a
            }, O = function() {
                if (r = {
                    b_avp: 1,
                    b_ph: 0,
                    b_phx: 0,
                    b_sep: 0,
                    p_p: 6,
                    p_v: 0,
                    p_a: 0,
                    p_e: 0,
                    p_t: 0,
                    l_o: 3,
                    l_h: 3,
                    l_l: 3,
                    l_c: 3,
                    l_v: 5,
                    l_a: 5,
                    l_e: 3,
                    l_t: 0,
                    u_p: 0,
                    u_v: 0,
                    u_a: 0,
                    wd: 62,
                    d: 0
                },
                s > 0)
                    return [];
                var t, i, a, o, l, u, c;
                for (t = []; ; ) {
                    if (e >= n)
                        return void 0;
                    if (a = {
                        d: 1,
                        c: 0
                    },
                    y())
                        if (y()) {
                            if (y()) {
                                for (a.c++,
                                a.a = r.b_avp,
                                y() && (r.b_avp ^= y(),
                                r.b_ph ^= y(),
                                r.b_phx ^= y(),
                                a.s = r.b_sep,
                                r.b_sep ^= y(),
                                y() && (r.wd = w([7])[0]),
                                a.s ^ r.b_sep && (a.s ? r.u_p = r.u_c : r.u_o = r.u_h = r.u_l = r.u_c = r.u_p)),
                                u = 0; u < 3 + 2 * r.b_ph; u++)
                                    if (y() && (l = "pvaet".charAt(u),
                                    o = r["p_" + l],
                                    r["p_" + l] += N(),
                                    r["u_" + l] = P(r["u_" + l], o, r["p_" + l]) - 0,
                                    r.b_sep && !u))
                                        for (c = 0; 4 > c; c++)
                                            l = "ohlc".charAt(c),
                                            r["u_" + l] = P(r["u_" + l], o, r.p_p) - 0;
                                !r.b_avp && a.a && (r.u_a = P(i && i.amount || 0, 0, r.p_a))
                            }
                            if (y())
                                for (a.c++,
                                u = 0; u < 7 + r.b_ph + r.b_phx; u++)
                                    y() && (6 == u ? a.d = x() : r["l_" + "ohlcva*et".charAt(u)] += N());
                            if (y() && (a.c++,
                            l = r.l_o + (y() && N()),
                            o = w([3 * l], [1])[0],
                            a.p = r.b_sep ? r.u_c + o : r.u_p += o),
                            !a.c)
                                break
                        } else
                            y() ? y() ? y() ? a.d = x() : r.l_v += N() : r.b_ph && y() ? r["l_" + "et".charAt(r.b_phx && y())] += N() : r.l_a += N() : r["l_" + "ohlc".charAt(w([2])[0])] += N();
                    for (u = 0; u < 6 + r.b_ph + r.b_phx; u++)
                        c = "ohlcvaet".charAt(u),
                        o = (r.b_sep ? 191 : 185) >> u & 1,
                        a["v_" + c] = w([3 * r["l_" + c]], [o])[0];
                    i = {
                        date: k(a.d)
                    },
                    a.p && (i.prevclose = P(a.p, r.p_p)),
                    r.b_sep ? (i.open = P(r.u_o += a.v_o, r.p_p),
                    i.high = P(r.u_h += a.v_h, r.p_p),
                    i.low = P(r.u_l += a.v_l, r.p_p),
                    i.close = P(r.u_c += a.v_c, r.p_p)) : (a.o = r.u_p + a.v_o,
                    i.open = P(a.o, r.p_p),
                    i.high = P(a.o + a.v_h, r.p_p),
                    i.low = P(a.o - a.v_l, r.p_p),
                    i.close = P(r.u_p = a.o + a.v_c, r.p_p)),
                    i.volume = P(r.u_v += a.v_v, r.p_v),
                    r.b_avp ? (o = T(r.p_p),
                    l = T(r.p_v),
                    i.amount = P(P(Math.floor((r.b_sep ? (r.u_o + r.u_h + r.u_l + r.u_c) / 4 : a.o + (a.v_h - a.v_l + a.v_c) / 4) * r.u_v + .5), [o[0] + l[0], o[1] + l[1]], r.p_a) + a.v_a, r.p_a)) : (r.u_a += a.v_a,
                    i.amount = P(r.u_a, r.p_a)),
                    r.b_ph && (i.postVol = P(a.v_e, r.p_e),
                    i.postAmt = P(Math.floor(i.postVol * i.close + (r.b_phx ? P(a.v_t, r.p_t) : 0) + .5), 0)),
                    t.push(i)
                }
                return t
            }, E = function(t) {
                var e, i, n;
                if (t = (t || 0).toString(),
                n = [],
                i = t.toLowerCase().indexOf("e"),
                i > 0) {
                    for (e = t.substr(i + 1) - 0; e >= 0; e--)
                        n.push(Math.floor(e * Math.pow(10, -e) + .5) - 0);
                    return n.join("")
                }
                return t
            };
            return g()()
        }
        ;
        var D = {
            dd: function(t) {
                return new Date(t.getFullYear(),t.getMonth(),t.getDate())
            },
            ddt: function(t) {
                return new Date(t.getTime())
            },
            stbd: function(t, e) {
                return t && e && t.getFullYear() == e.getFullYear() && t.getMonth() == e.getMonth() ? t.getDate() == e.getDate() : !1
            },
            stbdt: function(t, e) {
                return t && e ? t.getTime() == e.getTime() : !1
            },
            stbs: function(t, e, i, n) {
                return t.getFullYear() == e && t.getMonth() == i ? t.getDate() == n : !1
            },
            stbds: function(t, e, i) {
                !i && (i = "-");
                var n = e.split(i);
                return this.stbs(t, Number(n[0]), Number(n[1]) - 1, Number(n[2]))
            },
            ds: function(t, e, i, n, r, a) {
                "undefined" == typeof e && (e = "-");
                var o = [];
                if (n || o.push(t[i ? "getUTCFullYear" : "getFullYear"]()),
                !r) {
                    var s = t[i ? "getUTCMonth" : "getMonth"]() + 1;
                    o.push(10 > s ? "0" + s : s)
                }
                if (!a) {
                    var l = t[i ? "getUTCDate" : "getDate"]();
                    o.push(10 > l ? "0" + l : l)
                }
                return o.join(e)
            },
            dss: function(t, e, i) {
                var n = this.ds(t, e, i)
                  , r = [t["get" + (i ? "UTC" : "") + "Hours"]()]
                  , a = [t["get" + (i ? "UTC" : "") + "Minutes"]()]
                  , o = [t["get" + (i ? "UTC" : "") + "Seconds"]()]
                  , s = [10 > r ? "0" + r : r, 10 > a ? "0" + a : a, 10 > o ? "0" + o : o].join(":");
                return [n, s].join(" ")
            },
            dst: function(t, e, i) {
                var n = [t["get" + (i ? "UTC" : "") + "Hours"]()]
                  , r = [t["get" + (i ? "UTC" : "") + "Minutes"]()]
                  , a = [10 > n ? "0" + n : n, 10 > r ? "0" + r : r];
                if (e) {
                    var o = [t["get" + (i ? "UTC" : "") + "Seconds"]()];
                    a.push(10 > o ? "0" + o : o)
                }
                return a.join(":")
            },
            sd: function(t, e) {
                var i = t.split("-")
                  , n = i[0]
                  , r = i[1] - 1 || 0
                  , a = i[2] || 1
                  , o = 0
                  , s = 0
                  , l = 0;
                return e && (i = e.split(":"),
                o = i[0] || 0,
                s = i[1] || 0,
                l = i[2] || 0),
                new Date(n,r,a,o,s,l)
            },
            ssd: function(t) {
                var e = t.split(" ")
                  , i = e[0]
                  , n = e[1];
                return this.sd(i, n)
            },
            gw: function(t, e) {
                var i = 6048e5
                  , n = 2592e5
                  , r = (t.getTime() - n) / i
                  , a = (e.getTime() - n) / i;
                return Math.floor(r) == Math.floor(a)
            },
            gm: function(t, e) {
                return t.getFullYear() == e.getFullYear() ? t.getMonth() == e.getMonth() : !1
            },
            gy: function(t, e) {
                return t.getFullYear() == e.getFullYear()
            },
            weekname: ["\u65e5", "\u4e00", "\u4e8c", "\u4e09", "\u56db", "\u4e94", "\u516d", "\u65e5"],
            nw: function(t) {
                return this.weekname[t] || ""
            }
        };
        this.dateUtil = D,
        this.LoadingSign = o;
        var R = {
            replaceStr: function(t) {
                return t.replace(/[^0-9a-z_]/gi, function(t) {
                    return "$" + t.charCodeAt(0).toString(16)
                })
            },
            nfloat: function(t) {
                var e = 0;
                return t >= 1e5 ? e = 0 : t >= 100 && 1e5 > t ? e = 2 : t > 10 && 99 > t ? e = 3 : (10 >= t && t > 0 || t > -1 && 0 > t) && (e = 4),
                e
            },
            trim: function(t) {
                return t.replace(/^[\s\xA0]+/, "").replace(/[\s\xA0]+$/, "")
            },
            ps: function(t, e) {
                if (t = Number(t),
                isNaN(t))
                    return "-";
                var i = Math.abs(t);
                return 1e5 > i ? t.toFixed(e) : 1e7 > i ? (t / 1e4).toFixed(e) + "\u4e07" : 1e8 > i ? (t / 1e7).toFixed(e) + "\u5343\u4e07" : (t / 1e8).toFixed(e) + "\u4ebf"
            },
            nu: function(t) {
                return t = Number(t),
                t = Math.abs(t),
                1e5 > t || isNaN(t) ? [1, ""] : 1e7 > t ? [1e4, "\u4e07"] : 1e8 > t ? [1e7, "\u5343\u4e07"] : [1e8, "\u4ebf"]
            },
            vs: function(t, e) {
                var i, n = "";
                return t > 1e12 ? (i = (t / 1e12).toFixed(0),
                n = "\u4e07\u4ebf") : t > 1e8 ? (i = (t / 1e8).toFixed(2),
                n = "\u4ebf") : t > 1e5 ? (i = (t / 1e4).toFixed(2),
                n = "\u4e07") : i = t >= 1 ? t.toFixed(0) : "-",
                e ? i + n : i
            },
            zp: function(t) {
                return t = String(t),
                t.length < 2 ? "0" + t : t
            }
        };
        this.strUtil = R,
        this.tUtil = {
            s0: function(t) {
                return t = parseInt(Number(t)),
                0 > t ? "" : 10 > t ? "0" + String(t) : String(t)
            },
            tIWS: function(t, e) {
                for (var i = [], n = t; e >= n; n++)
                    i.push(this.s0(n / 60) + ":" + this.s0(n % 60));
                return i
            },
            gtr: function(t) {
                for (var e, i, n, r, a, o = [], s = 0, l = t.length; l > s; s++)
                    e = t[s][0],
                    i = t[s][1],
                    n = 60 * Number(e.split(":")[0]) + Number(e.split(":")[1]),
                    r = 60 * Number(i.split(":")[0]) + Number(i.split(":")[1]),
                    a = this.tIWS(n, r),
                    o = o.concat(a);
                return o
            },
            tradingA: [],
            gta: function() {
                return this.tradingA.length || (this.tradingA = this.gtr(v.CN)),
                this.tradingA
            },
            tradingRepo: [],
            gtrepo: function() {
                return this.tradingRepo.length || (this.tradingRepo = this.gtr(v.REPO)),
                this.tradingRepo
            },
            tradingUs: [],
            gtus: function() {
                return this.tradingUs.length || (this.tradingUs = this.gtr(v.US)),
                this.tradingUs
            },
            tradingLSE: [],
            gtlse: function() {
                return this.tradingLSE.length || (this.tradingLSE = this.gtr(v.LSE)),
                this.tradingLSE
            },
            tradingMSCI: [],
            gtmsci: function() {
                return this.tradingMSCI.length || (this.tradingMSCI = this.gtr(v.MSCI)),
                this.tradingMSCI
            },
            tradingGDS: [],
            gtgds: function() {
                return this.tradingGDS.length || (this.tradingGDS = this.gtr(v.GOODS)),
                this.tradingGDS
            },
            tradingHk: [],
            gthk: function() {
                return this.tradingHk.length || (this.tradingHk = this.gtr(v.HK)),
                this.tradingHk
            },
            tradingHkAp: [],
            gthkap: function() {
                return this.tradingHkAp.length || (this.tradingHkAp = this.gtr(v.HKAP)),
                this.tradingHkAp
            },
            tradingGlobalbd: [],
            gtglobaldb: function() {
                return this.tradingGlobalbd.length || (this.tradingGlobalbd = this.gtr(v.globalbd)),
                this.tradingGlobalbd
            },
            trading: [],
            gtAll: function(t) {
                return this.trading = this.gtr(t),
                this.trading
            },
            gata: function(t, e) {
                var i;
                switch (t) {
                case "REPO":
                    i = this.gtrepo();
                    break;
                case "US":
                    i = this.gtus();
                    break;
                case "HKAP":
                    i = this.gthkap();
                    break;
                case "HK":
                    i = this.gthk();
                    break;
                case "MSCI":
                    i = this.gtmsci();
                    break;
                case "NF":
                case "cb":
                    i = this.gtAll(e);
                    break;
                case "LSE":
                    i = this.gtlse();
                    break;
                case "HF":
                case "global_index":
                    i = this.gtAll(e);
                    break;
                case "globalbd":
                    i = this.gtglobaldb();
                    break;
                case "GOODS":
                    i = this.gtgds();
                    break;
                default:
                case "CN":
                    i = this.gta()
                }
                return i
            },
            ist: function(t, e) {
                return t = t.toUpperCase(),
                y(this.gata(t), e) >= 0
            },
            gltbt: function(t, e, i, n, r, a) {
                for (var o, s = [], l = this.gata(n, a), u = l.length, c = 0, d = 0, h = t * u; h > c; c++)
                    o = {
                        time: l[c % u],
                        price: -.1,
                        percent: 0,
                        avg_price: 0,
                        volume: -.01,
                        holdPosition: 0,
                        inventory: 0
                    },
                    c % u == 0 && r && (o.date = r[d],
                    d++),
                    s.push(o),
                    i || (s[c].price = s[c].avg_price = e,
                    s[c].volume = 0);
                return s[0].date && (s[0].today = D.ds(s[0].date)),
                s[0].price = s[0].avg_price = s[0].prevclose = e,
                s[0].volume = s[0].totalVolume = s[0].totalAmount = 0,
                s[0].holdPosition = 0,
                s[0].inventory = 0,
                s
            },
            azft: function(t, e) {
                if (!t)
                    return t;
                for (var i = this.gata(e), n = 0, r = t.length; r > n; n++)
                    i[n] && (t[n].time = i[n]);
                return t[0].date.setHours(0),
                t
            }
        },
        this.kUtil = {
            mw: function(t, e, i, n, r) {
                "number" != typeof n && (n = 0);
                var a = t.length
                  , o = t[0];
                n > 1 && (o.volume /= n);
                var s, l = [], u = [], c = [];
                if (1 == a)
                    l[0] = {
                        open: e.open,
                        high: e.high,
                        low: e.low,
                        close: e.price,
                        volume: e.totalVolume,
                        amount: e.totalAmount,
                        date: D.dd(e.date)
                    },
                    u[0] = {
                        open: e.open,
                        high: e.high,
                        low: e.low,
                        close: e.price,
                        volume: e.totalVolume,
                        amount: e.totalAmount,
                        date: D.dd(e.date)
                    },
                    c[0] = {
                        open: e.open,
                        high: e.high,
                        low: e.low,
                        close: e.price,
                        volume: e.totalVolume,
                        amount: e.totalAmount,
                        date: D.dd(e.date)
                    };
                else
                    for (var d, h = o.open, f = o.high, m = o.low, p = o.close, g = o.volume, v = o.date, b = o.amount, N = o.open, y = o.high, w = o.low, x = o.close, S = o.volume, k = o.date, T = o.amount, P = o.open, C = o.high, _ = o.low, R = o.close, A = o.volume, O = o.date, E = o.amount, I = 1; a > I; I++)
                        o = t[I],
                        n > 1 && (o.volume /= n,
                        o.postVol && (o.postVol /= n)),
                        D.gw(t[I - 1].date, o.date) ? (o.high > f && (f = o.high),
                        o.low < m && (m = o.low),
                        p = o.close,
                        g += o.volume,
                        b += o.amount,
                        v = o.date) : (isNaN(r) || (s = v.getDay(),
                        0 == s && (s = 7),
                        d = s - r,
                        d > 0 && (v = D.ddt(v),
                        v.setDate(v.getDate() - d))),
                        l.push({
                            open: h,
                            high: f,
                            low: m,
                            close: p,
                            volume: g,
                            date: v,
                            amount: b
                        }),
                        h = o.open,
                        f = o.high,
                        m = o.low,
                        p = o.close,
                        g = o.volume,
                        b = o.amount,
                        v = o.date),
                        D.gm(t[I - 1].date, o.date) ? (o.high > y && (y = o.high),
                        o.low < w && (w = o.low),
                        x = o.close,
                        S += o.volume,
                        T += o.amount,
                        k = o.date) : (isNaN(r) || (s = k.getDay(),
                        0 == s && (s = 7),
                        d = s - r,
                        d > 0 && (k = D.ddt(k),
                        k.setDate(k.getDate() - d))),
                        u.push({
                            open: N,
                            high: y,
                            low: w,
                            close: x,
                            volume: S,
                            date: k,
                            amount: T
                        }),
                        N = o.open,
                        y = o.high,
                        w = o.low,
                        x = o.close,
                        S = o.volume,
                        T = o.amount,
                        k = o.date),
                        D.gy(t[I - 1].date, o.date) ? (o.high > C && (C = o.high),
                        o.low < _ && (_ = o.low),
                        R = o.close,
                        A += o.volume,
                        E += o.amount,
                        O = o.date) : (c.push({
                            open: P,
                            high: C,
                            low: _,
                            close: R,
                            volume: A,
                            date: O,
                            amount: E
                        }),
                        P = o.open,
                        C = o.high,
                        _ = o.low,
                        R = o.close,
                        A = o.volume,
                        O = o.date),
                        I == a - 1 && (l.push({
                            open: h,
                            high: f,
                            low: m,
                            close: p,
                            volume: g,
                            date: v,
                            amount: b
                        }),
                        u.push({
                            open: N,
                            high: y,
                            low: w,
                            close: x,
                            volume: S,
                            date: k,
                            amount: T
                        }),
                        c.push({
                            open: P,
                            high: C,
                            low: _,
                            close: R,
                            volume: A,
                            date: O,
                            amount: E
                        }));
                return l[0].prevclose = i,
                u[0].prevclose = i,
                c[0].prevclose = i,
                [l, u, c]
            },
            nc: function(t, e, i, n) {
                if (t && !(t.length < 1)) {
                    n = n || {};
                    var r = t[t.length - 1];
                    if (168 == i && D.gw(r.date, e.date) || 720 == i && D.gm(r.date, e.date))
                        return r.day = String(e.today).split("-").join("/"),
                        void (r.date = D.dd(e.date));
                    r = t[t.length - 1];
                    var a = r.close
                      , o = e.price - a
                      , s = o / a;
                    t.push({
                        open: isNaN(n.price) ? a : n.price,
                        high: isNaN(n.price) ? e.high : n.price,
                        low: isNaN(n.price) ? e.low : n.price,
                        close: isNaN(n.price) ? e.price : n.price,
                        volume: isNaN(n.volume) ? e.totalVolume : n.volume,
                        amount: isNaN(n.amount) ? e.totalAmount : n.amount,
                        percent: s,
                        day: String(e.today).split("-").join("/"),
                        date: D.ddt(e.date),
                        time: e.time,
                        ampP: 0,
                        amplitude: 0,
                        change: o,
                        kke_cs: 0
                    })
                }
            },
            pd: function(t, e) {
                var i = t.length
                  , n = t[0]
                  , r = n.prevclose;
                (isNaN(r) || 0 >= r) && (r = n.open);
                for (var a = 0; i > a; a++) {
                    if (n = t[a],
                    e && e.usePc && (r = n.prevclose),
                    0 === n.open && (n.open = a > 0 ? t[a - 1].close : n.close),
                    0 === n.close && (n.close = n.open),
                    0 === n.high && (n.high = n.open,
                    n.high < n.close && (n.high = n.close)),
                    0 === n.low && (n.low = n.open,
                    n.low < n.close && (n.low = n.close)),
                    n.amplitude = n.high - n.low,
                    n.ampP = n.amplitude / r,
                    n.change = n.close - r,
                    n.percent = n.change / r,
                    r = n.close,
                    n.day) {
                        var o = n.day.split(" ");
                        n.day = o[0],
                        n.time = o[1].slice(0, 5),
                        n.date = D.sd(n.day, n.time),
                        n.day = n.day.split("-").join("/")
                    } else {
                        var s = n.date
                          , l = R.zp(s.getMonth() + 1)
                          , u = R.zp(s.getDate());
                        n.day = [s.getFullYear(), l, u].join("/")
                    }
                    n.kke_cs = n.close > n.open ? 1 : n.open > n.close ? -1 : 0
                }
            },
            ms: function(t, e, i, n, r) {
                return i > t && (t += 24),
                Math.max(1, Math.ceil((60 * (t - i) + e - n) / r))
            },
            spk: function(t, e, i, n, r) {
                if (t == e)
                    return !0;
                var a = t.split(":")
                  , o = Number(a[0])
                  , s = Number(a[1]);
                a = e.split(":");
                var l = Number(a[0])
                  , u = Number(a[1]);
                if (o > l && 3 > o - l || o == l && s >= u)
                    return !0;
                if (60 != n || r && /^forex/.test(r)) {
                    a = i.split(":");
                    var c = Number(a[0])
                      , d = Number(a[1])
                      , h = this.ms(o, s, c, d, n)
                      , f = this.ms(l, u, c, d, n);
                    return h == f
                }
                return "10:30" != t && "11:30" != t && "14:00" != t && "15:00" != t || u == s ? !0 : !1
            },
            yd: function(t) {
                for (var e = t[t.length - 1].date.getFullYear(), i = [], n = t.length; n-- && t[n].date.getFullYear() == e; )
                    i[i.length] = t[n];
                return i.reverse(),
                i[0].prevclose = t[n] ? t[n].prevclose || t[n].close : i[0].prevclose || i[0].close,
                i
            },
            rd: function(t, e) {
                var i = []
                  , n = D.dd(e);
                n.setFullYear(n.getFullYear() - 5);
                for (var r = t.length; r-- && !(t[r].date < n); )
                    i[i.length] = t[r];
                return i.reverse(),
                i[0].prevclose = t[r] ? t[r].close : i[0].close,
                i
            },
            adbd: function(t, e, i, n) {
                for (var r, a, o, s, l = i ? D.stbdt : D.stbd, u = t.length, c = e.length; c--; ) {
                    if (o = e[c].date,
                    1 > u) {
                        c = e.length - t.length;
                        for (var d = [], h = t[0]; c-- > 0; ) {
                            if (a = x(h) || {},
                            a.isFake = !0,
                            a.kke_cs = 0,
                            n)
                                for (r in a)
                                    a.hasOwnProperty(r) && p(a[r]) && (a[r] = 0);
                            d.push(a)
                        }
                        t = d.concat(t);
                        break
                    }
                    for (var f = u--; f-- && (s = t[f].date,
                    !l(o, s)); ) {
                        if (o > s) {
                            if (a = x(t[f]),
                            a.isFake = !0,
                            a.date = o,
                            a.kke_cs = 0,
                            n)
                                for (r in a)
                                    a.hasOwnProperty(r) && p(a[r]) && (a[r] = 0);
                            t.splice(++f, 0, a),
                            u++;
                            break
                        }
                        t.splice(f, 1),
                        u--
                    }
                }
                return u > 0 && t.splice(0, u),
                t
            },
            ayd: function(t, e, i, n, r) {
                for (var a, o, s, l, u = D.stbd, c = t.length, d = e.length; d--; )
                    if (s = e[d],
                    !(s > r)) {
                        if (n > s && !D.stbd(s, n))
                            break;
                        for (var h = c--; h-- && (l = t[h].date,
                        !u(s, l)); ) {
                            if (s > l) {
                                o = x(t[h]);
                                var f = o.close;
                                for (a in o)
                                    o.hasOwnProperty(a) && p(o[a]) && (o[a] = 0);
                                o.open = o.high = o.low = o.close = f,
                                o.date = s,
                                t.splice(++h, 0, o),
                                c++;
                                break
                            }
                            t.splice(h, 1),
                            c--
                        }
                    }
                return c > 0 && t.splice(0, c),
                t
            }
        },
        this.domGc = new function() {
            var t = u.$C("div");
            return t.style.display = "none",
            function(e, i) {
                if (e) {
                    if (e.hasChildNodes())
                        for (; e.childNodes.length > 0; )
                            e.removeChild(e.firstChild);
                    if (i)
                        return void (e.innerHTML = "");
                    t.appendChild(e),
                    t.innerHTML = ""
                }
            }
        }
        ,
        this.getSUrl = function(t) {
            if (!t)
                return null;
            var e, i = t.match(/(\w*:\/\/)?([^\/]+)(\/+.*)?/i), n = i[2], r = i[3];
            return e = ["https://", n, r].join("")
        }
        ,
        this.TipM = s,
        this.logoM = new function() {
            var t = "data:image/png;base64,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"
              , e = u.$C("img")
              , i = !1
              , n = []
              , r = []
              , a = function() {
                u.xh5_EvtUtil.addHandler(e, "load", function() {
                    for (i = !0; n.length; ) {
                        var t = n.shift();
                        s(t)
                    }
                }),
                e.src = t
            }
              , o = function(t) {
                if (t.logo && !u.xh5_BrowserUtil.noH5) {
                    var e = t.logo;
                    t.color || (t.color = "#ccc");
                    var i = u.hex2dec(t.color, 0 / 0, !0);
                    (!i || i.length < 3) && (i = [200, 200, 200]);
                    for (var n = e.getContext("2d"), r = n.getImageData(0, 0, e.width, e.height), a = i[0], o = i[1], s = i[2], l = 0, c = r.data.length; c > l; l += 4)
                        0 != r.data[l + 3] && (r.data[l] = a,
                        r.data[l + 1] = o,
                        r.data[l + 2] = s);
                    n.putImageData(r, 0, 0)
                }
            }
              , s = function(t) {
                if (u.xh5_BrowserUtil.noH5)
                    return null;
                if (!i) {
                    for (var a = n.length; a--; )
                        if (n[a].id == t.id)
                            return null;
                    return n.push(t),
                    null
                }
                var s;
                s = u.$C("canvas", t.id),
                s.style.zIndex = 0,
                r.push(s),
                s.style.position = "absolute",
                s.style.top = t.top + "px",
                s.style.right = t.right + "px",
                s.width = e.width,
                s.height = e.height,
                s.style.width = t.LOGO_W + "px",
                s.style.height = t.LOGO_H + "px";
                var l = s.getContext("2d");
                if (t.isShare) {
                    var c = u.xh5_BrowserUtil.hdpr;
                    if (2 > c) {
                        var d = c / 2;
                        l.scale(d, d)
                    }
                }
                return l.drawImage(e, 0, 0),
                o({
                    logo: s,
                    color: t.color
                }),
                f(t.cb) && t.cb(s),
                s
            };
            this.getLogo = s,
            this.styleLogo = o,
            a()
        }
        ,
        this.grabM = new function() {
            var t = function(t) {
                var e = t.dom
                  , i = t.child;
                if (!e || !i)
                    return null;
                h(e) && (e = u.$DOM(e));
                var n = e.getElementsByTagName(i);
                if (!n || n.length < 1)
                    return null;
                var r = u.xh5_BrowserUtil.hdpr
                  , a = e.offsetWidth
                  , o = e.offsetHeight
                  , s = u.$C("canvas")
                  , l = s.getContext("2d");
                s.style.width = a + "px",
                s.style.height = o + "px",
                s.width = a * r,
                s.height = o * r,
                1 != r && l.scale(r, r);
                var c = u.xh5_HtmlPosUtil.pageX(e)
                  , d = u.xh5_HtmlPosUtil.pageY(e)
                  , f = u.xh5_HtmlPosUtil.parentY(e);
                l.textBaseline = "top";
                for (var m, p, g = 0, v = n.length; v > g; g++) {
                    m = n[g],
                    p = u.getCSS(m);
                    var b = u.xh5_HtmlPosUtil.pageX(m) - c
                      , N = u.xh5_HtmlPosUtil.pageY(m) - d
                      , y = Number(p.paddingLeft.split("px")[0])
                      , w = .5 * (Number(p.lineHeight.split("px")[0]) - Number(p.fontSize.split("px")[0]));
                    l.fillStyle = p.backgroundColor,
                    l.fillRect(b, N, m.offsetWidth, m.offsetHeight),
                    l.font = [p.fontSize, p.fontFamily].join(" "),
                    l.fillStyle = p.color,
                    l.fillText(m.innerHTML, b + y, N + w)
                }
                return {
                    canvas: s,
                    x: c,
                    y: f
                }
            }
              , e = function(t, e) {
                if (u.POST) {
                    var i = e.txt || ""
                      , n = e.url || ""
                      , r = "_" + Math.floor(1e3 * Math.random());
                    window.open("about:blank", r);
                    var a = u.getSUrl("http://stock.finance.sina.com.cn/misc/userapi/Pic4Weibo.php");
                    u.POST(a, {
                        imgData: t,
                        symbol: "imgData"
                    }, function(t) {
                        t && t.match(/^http.+/) && (t = encodeURIComponent(t),
                        t = "http://service.weibo.com/share/share.php?source=bookmark&title=" + encodeURIComponent(i) + "&url=" + encodeURIComponent(n) + "&pic=" + t,
                        window.open(t, r))
                    })
                }
            }
              , i = function(i) {
                if (!u.xh5_BrowserUtil.noH5) {
                    var n = i.ctn;
                    if (n) {
                        for (var r, a, o = n.getElementsByTagName("canvas"), s = i.w || n.offsetWidth, l = i.h || n.offsetHeight, c = u.xh5_BrowserUtil.hdpr, d = [], h = u.xh5_HtmlPosUtil.pageX(n), f = u.xh5_HtmlPosUtil.pageY(n), p = o.length; p--; ) {
                            a = o[p],
                            r = a.style.zIndex;
                            var g, v = !1;
                            for (g = i.ignoreZIdxArr.length; g--; )
                                if (r == i.ignoreZIdxArr[g]) {
                                    v = !0;
                                    break
                                }
                            if (!v) {
                                for (g = i.ignoreIdArr.length; g--; )
                                    if (a.id == i.ignoreIdArr[g]) {
                                        v = !0;
                                        break
                                    }
                                if (!v) {
                                    var b = {
                                        canvas: a,
                                        x: u.xh5_HtmlPosUtil.pageX(a) - h,
                                        y: u.xh5_HtmlPosUtil.pageY(a) - f
                                    };
                                    d.push(b)
                                }
                            }
                        }
                        if (!i.nologo) {
                            var N = u.logoM.getLogo({
                                cb: null,
                                id: "share_logo",
                                isShare: !0,
                                top: i.top,
                                right: i.right,
                                LOGO_W: i.LOGO_W,
                                LOGO_H: i.LOGO_H,
                                color: i.color
                            });
                            N && d.push({
                                canvas: N,
                                x: s - Number(N.style.right.split("px")[0]) - i.LOGO_W,
                                y: Number(N.style.top.split("px")[0])
                            })
                        }
                        if (i.extra) {
                            !m(i.extra) && (i.extra = [i.extra]);
                            for (var y = 0, w = i.extra.length; w > y; y++) {
                                var x = t(i.extra[y]);
                                x && (d = d.concat(x))
                            }
                        }
                        var S = u.$C("canvas")
                          , k = S.getContext("2d");
                        S.style.width = s + "px",
                        S.style.height = l + "px",
                        S.width = s * c,
                        S.height = l * c,
                        k.fillStyle = i.bgColor,
                        k.fillRect(0, 0, s, l);
                        for (var T = 0, P = d.length; P > T; T++) {
                            var C = d[T];
                            k.drawImage(C.canvas, C.x * c, C.y * c)
                        }
                        e(S.toDataURL("image/png").substring(22), i)
                    }
                }
            };
            this.shareTo = i
        }
        ,
        this.bridge = new function() {
            function t(t, e) {
                for (var i in t)
                    t.hasOwnProperty(i) && (t[i] = e + t[i])
            }
            var e, i, n = !1, r = "sinatkchart_SLBridge~", a = {
                SAVE: "save",
                LOAD: "load",
                REMOVE: "remove",
                DATA: "data",
                READY: "ready"
            };
            t(a, r);
            var o = []
              , s = {}
              , l = []
              , c = function(t) {
                var e = t
                  , i = e.key
                  , n = e.options
                  , r = e.value;
                T.save(i, r, n)
            }
              , d = function(t) {
                n || i || l.push([t])
            }
              , h = function(t) {
                var e = t
                  , i = e.key
                  , n = e.options;
                return T.load(i, n)
            }
              , f = function(t, e) {
                return n ? void 0 : i ? void (s[t.uid] = e) : void o.push([t, e])
            }
              , m = function(t, e, i) {
                var n = h(t);
                e(n),
                i || f(t, e)
            }
              , p = function(t, e) {
                t && (c(t),
                e || d(t))
            }
              , g = new function() {
                var t = function(t) {
                    if (t && t.type) {
                        var e = t.type;
                        if (-1 != e.indexOf(r))
                            return e
                    }
                    return void 0
                }
                  , e = function() {
                    for (var t; o.length; )
                        t = o.shift(),
                        m(t[0], t[1]);
                    for (; l.length; )
                        t = l.shift(),
                        p(t[0])
                };
                this.onMsg = function(i) {
                    var n;
                    try {
                        n = JSON.parse(i.data)
                    } catch (r) {}
                    var o = t(n);
                    if (o)
                        switch (o) {
                        case a.READY:
                            e();
                            break;
                        case a.DATA:
                            if (!u.isFunc(s[n.uid]))
                                return;
                            s[n.uid](n.result),
                            s[n.uid] = null,
                            delete s[n.uid]
                        }
                }
            }
            ;
            u.xh5_EvtUtil.addHandler(window, "message", g.onMsg),
            this.load = m,
            this.save = p,
            this.getStatus = function() {
                return i && !n && "1" == e.getAttribute("data-ready")
            }
        }
        ,
        this.colorPicker = function() {
            function t(t, e) {
                var i = function() {}
                  , n = t.prototype;
                i.prototype = e.prototype,
                t.prototype = new i;
                for (var r in n)
                    n.hasOwnProperty(r) && (t.prototype[r] = n[r]);
                t.prototype.constructor = t
            }
            function e(t, i, n) {
                if (!i)
                    return t;
                t || (t = {});
                for (var r in i)
                    i.hasOwnProperty(r) && ("Object" === _(i[r]) ? (!t[r] && (t[r] = {}),
                    e(t[r], i[r], n)) : !n && r in t || (t[r] = i[r]));
                return t
            }
            function i(t) {
                var e = "undefined" == typeof getComputedStyle ? t.currentStyle : getComputedStyle(t);
                return e ? (t.clientWidth || b(e.width) || b(t.style.width)) - (b(e.paddingLeft) || 0) - (b(e.paddingRight) || 0) | 0 : 0
            }
            function n(t) {
                var e = "undefined" == typeof getComputedStyle ? t.currentStyle : getComputedStyle(t);
                return e ? (t.clientHeight || b(e.height) || b(t.style.height)) - (b(e.paddingTop) || 0) - (b(e.paddingBottom) || 0) | 0 : 0
            }
            function r(t) {
                return t.getBoundingClientRect ? t.getBoundingClientRect() : {
                    left: 0,
                    top: 0
                }
            }
            function a(t) {
                var e = t.getContext("2d");
                e.clearRect(0, 0, t.width, t.height)
            }
            function o(t, e) {
                var r = document.createElement("canvas")
                  , a = r.style
                  , o = i(t)
                  , s = n(t)
                  , l = o * e.width
                  , u = s * e.height;
                return r.width = l,
                r.height = u,
                a.position = "absolute",
                a.width = l + "px",
                a.height = u + "px",
                a.left = o * e.left + "px",
                a.top = s * e.top + "px",
                t.appendChild(r),
                r
            }
            function s(t, e) {
                var r = document.createElement("ul")
                  , a = r.style
                  , o = e.label
                  , s = i(t)
                  , u = n(t);
                a.listStyle = "none",
                a.padding = 0,
                a.margin = 0,
                a.font = e.font,
                a.position = "absolute",
                a.left = s * e.left + "px",
                a.top = u * e.top + "px";
                for (var c = 0, d = o.length; d > c; c++)
                    l(r, c, e);
                return t.appendChild(r),
                r
            }
            function l(t, e, i) {
                var n = document.createElement("li")
                  , r = document.createElement("label")
                  , a = document.createElement("input")
                  , o = r.style
                  , s = n.style
                  , l = a.style;
                return r.innerHTML = i.label[e],
                o.textAlign = "right",
                o.display = "inline-block",
                o.width = i.labelWidth + "px",
                o.color = i.color,
                "number" == i.type && (a.type = "number"),
                l.width = i.inputWidth + "px",
                s.marginBottom = i.gap + "px",
                k(a, "mousemove", function(t) {
                    T(t)
                }),
                n.appendChild(r),
                n.appendChild(a),
                t.appendChild(n),
                n
            }
            function c(t, e) {
                var r = document.createElement("div")
                  , a = r.style
                  , o = i(t)
                  , s = n(t);
                return a.position = "absolute",
                a.left = o * e.left + "px",
                a.top = s * e.top + "px",
                a.width = o * e.width + "px",
                a.height = s * e.height + "px",
                t.appendChild(r),
                r
            }
            function d(t, e) {
                function i(i) {
                    i = R(e, i),
                    t._onmousemove(i.NyanX, i.NyanY),
                    t.onmousemove && t.onmousemove(t)
                }
                function n(t) {
                    o = !0,
                    i(t)
                }
                function r(t) {
                    o && i(t),
                    T(t),
                    P(t)
                }
                function a() {
                    o && (o = !1)
                }
                var o = !1;
                "ontouchend"in window ? (k(e, "touchstart", n),
                k(e, "touchmove", r),
                k(e, "touchend", a)) : (k(e, "mousedown", n),
                k(e, "mousemove", r),
                k(e, "mouseup", a),
                k(e, "mouseout", a))
            }
            function h(t, e, i) {
                return t = Math.round(t),
                e > t ? e : t > i ? i : t
            }
            function f(t, e, i) {
                return e > t ? e : t > i ? i : t
            }
            function m(t) {
                return t.length && "%" === t.charAt(t.length - 1) ? h(parseFloat(t) / 100 * 255, 0, 255) : h(parseInt(t, 10), 0, 255)
            }
            function p(t) {
                return t.length && "%" === t.charAt(t.length - 1) ? f(parseFloat(t) / 100, 0, 1) : f(parseFloat(t), 0, 1)
            }
            function g(t, e, i) {
                return 0 > i ? i += 1 : i > 1 && (i -= 1),
                1 > 6 * i ? t + (e - t) * i * 6 : 1 > 2 * i ? e : 2 > 3 * i ? t + (e - t) * (2 / 3 - i) * 6 : t
            }
            function v(t) {
                var e = (parseFloat(t[0]) % 360 + 360) % 360 / 360
                  , i = p(t[1])
                  , n = p(t[2])
                  , r = .5 >= n ? n * (i + 1) : n + i - n * i
                  , a = 2 * n - r;
                return [f(255 * g(a, r, e + 1 / 3), 0, 255), f(255 * g(a, r, e), 0, 255), f(255 * g(a, r, e - 1 / 3), 0, 255)]
            }
            function N(t) {
                if (t) {
                    var e, i, n = t[0] / 255, r = t[1] / 255, a = t[2] / 255, o = Math.min(n, r, a), s = Math.max(n, r, a), l = s - o, u = (s + o) / 2;
                    if (0 === l)
                        e = 0,
                        i = 0;
                    else {
                        i = .5 > u ? l / (s + o) : l / (2 - s - o);
                        var c = ((s - n) / 6 + l / 2) / l
                          , d = ((s - r) / 6 + l / 2) / l
                          , h = ((s - a) / 6 + l / 2) / l;
                        n === s ? e = h - d : r === s ? e = 1 / 3 + c - h : a === s && (e = 2 / 3 + d - c),
                        0 > e && (e += 1),
                        e > 1 && (e -= 1)
                    }
                    return [360 * e, i, u]
                }
            }
            function y(t) {
                if (t) {
                    t += "";
                    var e = t.replace(/ /g, "").toLowerCase();
                    if ("#" !== e.charAt(0)) {
                        var i = e.indexOf("(")
                          , n = e.indexOf(")");
                        if (-1 !== i && n + 1 === e.length) {
                            var r = e.substr(0, i)
                              , a = e.substr(i + 1, n - (i + 1)).split(",");
                            switch (r) {
                            case "rgb":
                                if (3 !== a.length)
                                    return;
                                return [m(a[0]), m(a[1]), m(a[2])];
                            case "hsl":
                                if (3 !== a.length)
                                    return;
                                return v(a);
                            default:
                                return
                            }
                        }
                    } else {
                        if (4 === e.length) {
                            var o = parseInt(e.substr(1), 16);
                            if (!(o >= 0 && 4095 >= o))
                                return;
                            return [(3840 & o) >> 4 | (3840 & o) >> 8, 240 & o | (240 & o) >> 4, 15 & o | (15 & o) << 4]
                        }
                        if (7 === e.length) {
                            if (o = parseInt(e.substr(1), 16),
                            !(o >= 0 && 16777215 >= o))
                                return;
                            return [(16711680 & o) >> 16, (65280 & o) >> 8, 255 & o]
                        }
                    }
                }
            }
            function w(t) {
                var e = [(+t[0]).toFixed(0), (+t[1]).toFixed(0), (+t[2]).toFixed(0)];
                return ((1 << 24) + (e[0] << 16) + (e[1] << 8) + +e[2]).toString(16).slice(1)
            }
            function x(t) {
                var e = [t[0].toFixed(0), (100 * t[1]).toFixed(0) + "%", (100 * t[2]).toFixed(0) + "%"];
                return "hsl(" + e.join(",") + ")"
            }
            function S(t, e) {
                if (t) {
                    var i = "Array" == _(t) ? t : y(t);
                    switch (e) {
                    case "rgb":
                        return e + "(" + i.join(",") + ")";
                    case "hex":
                        return "#" + w(i);
                    case "hsl":
                        return x(N(i))
                    }
                }
            }
            if ("undefined" != typeof getComputedStyle) {
                var k = function() {
                    return window.addEventListener ? function(t, e, i) {
                        t.addEventListener(e, i)
                    }
                    : function(t, e, i) {
                        t.attachEvent("on" + e, i)
                    }
                }()
                  , T = function() {
                    return window.addEventListener ? function(t) {
                        t.stopPropagation()
                    }
                    : function(t) {
                        t.cancelBubble = !0
                    }
                }()
                  , P = function() {
                    return window.addEventListener ? function(t) {
                        t.preventDefault()
                    }
                    : function(t) {
                        t.returnValue = !1
                    }
                }()
                  , C = Object.prototype.toString
                  , _ = function(t) {
                    return null === t ? "Null" : void 0 === t ? "Undefined" : C.call(t).slice(8, -1)
                }
                  , D = function(t, e) {
                    if (!t)
                        return -1;
                    if (t.indexOf)
                        return t.indexOf(e);
                    for (var i = t.length; i--; )
                        if (t[i] === e)
                            return i
                }
                  , R = function(t, e) {
                    if (e = e || window.event,
                    null != e.NyanX)
                        return e;
                    var i = e.type
                      , n = i && D(i, "touch") >= 0;
                    if (n) {
                        var a = "touchend" != i ? e.targetTouches[0] : e.changedTouches[0];
                        if (a) {
                            var o = r(t);
                            e.NyanX = a.clientX - o.left,
                            e.NyanY = a.clientY - o.top
                        }
                    } else {
                        var s = r(t);
                        e.NyanX = e.clientX - s.left,
                        e.NyanY = e.clientY - s.top,
                        e.NyanDelta = e.wheelDelta ? e.wheelDelta / 120 : -(e.detail || 0) / 3
                    }
                    return e
                }
                  , A = {
                    width: 320,
                    height: 200,
                    zIndex: 10002,
                    backgroundColor: "#444",
                    wrapShadow: "3px 3px 4px rgba(0, 0, 0, 0.4)",
                    color: "#66ccff",
                    picker: {
                        left: .05,
                        top: .15,
                        width: .4,
                        height: .65,
                        size: 10,
                        color: "#000",
                        lineWidth: 1
                    },
                    slider: {
                        left: .5,
                        top: .15,
                        width: .05,
                        height: .65
                    },
                    rgbBox: {
                        label: ["R:", "G:", "B:"],
                        font: "12px Microsoft YaHei",
                        color: "#FFFEFA",
                        gap: 8,
                        type: "number",
                        labelWidth: 15,
                        inputWidth: 36,
                        left: .6,
                        top: .15
                    },
                    hslBox: {
                        label: ["H:", "S:", "L:"],
                        font: "12px Microsoft YaHei",
                        color: "#FFFEFA",
                        gap: 8,
                        type: "number",
                        labelWidth: 15,
                        inputWidth: 36,
                        left: .78,
                        top: .15
                    },
                    hexBox: {
                        label: ["#"],
                        font: "12px Microsoft YaHei",
                        color: "#FFFEFA",
                        labelWidth: 15,
                        inputWidth: 60,
                        left: .03,
                        top: .85
                    },
                    colorBox: {
                        left: .63,
                        top: .6,
                        width: .32,
                        height: .2
                    },
                    okBtn: {
                        text: "\u786e\u5b9a",
                        backgroundColor: "#6C6C6C",
                        color: "#FFFEFA",
                        font: "12px Microsoft YaHei",
                        left: .65,
                        top: .87,
                        width: .12,
                        height: .1
                    },
                    cancelBtn: {
                        text: "\u53d6\u6d88",
                        backgroundColor: "#6C6C6C",
                        color: "#FFFEFA",
                        font: "12px Microsoft YaHei",
                        left: .83,
                        top: .87,
                        width: .12,
                        height: .1
                    }
                }
                  , O = function(t, i) {
                    e(this, i),
                    this.background = o(t, i),
                    this.layer = o(t, i),
                    this.H = 0,
                    this.S = 0,
                    d(this, this.layer),
                    this.paintBG()
                };
                O.prototype = {
                    constructor: O,
                    paintBG: function() {
                        for (var t = this.background, e = t.getContext("2d"), i = t.width, n = t.height, r = e.createLinearGradient(0, 0, i, 0), a = 0; 1 > a; a += 1 / 6)
                            r.addColorStop(a, "hsl(" + 360 * a + " , 100%, 50%)");
                        e.fillStyle = r,
                        e.fillRect(0, 0, i, n),
                        r = e.createLinearGradient(0, 0, 0, n),
                        r.addColorStop(0, "hsla(0, 0%, 50%, 0)"),
                        r.addColorStop(1, "hsla(0, 0%, 50%, 1)"),
                        e.fillStyle = r,
                        e.fillRect(0, 0, i, n)
                    },
                    _onmousemove: function(t, e) {
                        var r = this.layer
                          , a = i(r)
                          , o = n(r);
                        this.H = t / a * 360,
                        this.S = (o - e) / o
                    },
                    updatePoint: function() {
                        var t = this.layer
                          , e = t.getContext("2d")
                          , r = this.size
                          , a = i(t)
                          , o = n(t)
                          , s = this.H * a / 360
                          , l = o - this.S * o;
                        e.clearRect(0, 0, t.width, t.height),
                        e.beginPath(),
                        e.moveTo(s - r, l),
                        e.lineTo(s + r, l),
                        e.moveTo(s, l - r),
                        e.lineTo(s, l + r),
                        e.strokeStyle = "black",
                        e.lineWidth = 2,
                        e.stroke()
                    },
                    update: function(t) {
                        this.H = t[0],
                        this.S = t[1],
                        this.updatePoint()
                    }
                };
                var E = function(t, i) {
                    e(this, i),
                    this.background = o(t, i),
                    this.layer = o(t, i),
                    this.L = .5,
                    d(this, this.layer)
                };
                E.prototype = {
                    constructor: E,
                    paintBG: function(t) {
                        var e = this.background
                          , i = e.getContext("2d")
                          , n = e.width
                          , r = e.height
                          , o = i.createLinearGradient(0, 0, 0, r);
                        a(e),
                        o.addColorStop(0, "#fff"),
                        o.addColorStop(.5, "hsl(" + (+t[0]).toFixed(0) + ", " + (100 * t[1]).toFixed(0) + "%, 50%)"),
                        o.addColorStop(1, "#000"),
                        i.fillStyle = o,
                        i.fillRect(0, 0, n, r)
                    },
                    _onmousemove: function(t, e) {
                        var i = this.layer
                          , r = n(i);
                        this.L = (r - e) / r
                    },
                    updatePoint: function(t) {
                        for (var e = this.layer, i = e.getContext("2d"), r = n(e), a = r - this.L * r, o = v(t), s = o.length; s--; )
                            o[s] = (255 - o[s]).toFixed(0);
                        i.clearRect(0, 0, e.width, e.height),
                        i.beginPath(),
                        i.moveTo(0, a + .5),
                        i.lineTo(e.width, a + .5),
                        i.strokeStyle = S(o, "hex"),
                        i.lineWidth = 3,
                        i.stroke()
                    },
                    update: function(t) {
                        this.L = t[2],
                        this.paintBG(t),
                        this.updatePoint(t)
                    }
                };
                var I = function(t, e) {
                    var i = this;
                    this.box = s(t, e),
                    k(this.box, "input", function(t) {
                        t.target.value = h(t.target.value, 0, 255),
                        i.oninput && i.oninput(t)
                    })
                };
                I.prototype = {
                    constructor: I,
                    getRGB: function() {
                        var t = this.box.childNodes;
                        return "rgb(" + t[0].childNodes[1].value + ", " + t[1].childNodes[1].value + ", " + t[2].childNodes[1].value + ")"
                    },
                    getRGBArr: function() {
                        var t = this.box.childNodes;
                        return [t[0].childNodes[1].value, t[1].childNodes[1].value, t[2].childNodes[1].value]
                    },
                    update: function(t) {
                        for (var e = this.box.childNodes, i = v(t), n = 0, r = i.length; r > n; n++)
                            e[n].childNodes[1].value = (+i[n]).toFixed(0)
                    }
                };
                var L = function(t, e) {
                    var i = this;
                    this.box = s(t, e);
                    var n = this.box.childNodes;
                    k(n[0].childNodes[1], "input", function(t) {
                        t.target.value = h(t.target.value, 0, 360),
                        i.oninput && i.oninput(t)
                    }),
                    k(n[1].childNodes[1], "input", function(t) {
                        t.target.value = h(t.target.value, 0, 100),
                        i.oninput && i.oninput(t)
                    }),
                    k(n[2].childNodes[1], "input", function(t) {
                        t.target.value = h(t.target.value, 0, 100),
                        i.oninput && i.oninput(t)
                    })
                };
                L.prototype = {
                    constructor: L,
                    getHSL: function() {
                        var t = this.box.childNodes;
                        return "hsl(" + t[0].childNodes[1].value + ", " + t[1].childNodes[1].value + "%, " + t[2].childNodes[1].value + "% )"
                    },
                    getHSLArr: function() {
                        var t = this.box.childNodes;
                        return [t[0].childNodes[1].value, t[1].childNodes[1].value / 100, t[2].childNodes[1].value / 100]
                    },
                    update: function(t) {
                        for (var e = this.box.childNodes, i = 0, n = t.length; n > i; i++)
                            e[i].childNodes[1].value = (i > 0 ? 100 * t[i] : +t[i]).toFixed(0)
                    }
                };
                var H = function(t, e) {
                    var i = this;
                    this.box = s(t, e);
                    var n = this.box.childNodes;
                    k(n[0].childNodes[1], "input", function(t) {
                        t.target.value = t.target.value.replace(/[^0-9A-Fa-f]/g, "").slice(0, 6);
                        var e = t.target.value.length;
                        6 == e && i.oninput && i.oninput(t)
                    })
                };
                H.prototype = {
                    constructor: H,
                    getHEX: function() {
                        return "#" + this.box.childNodes[0].childNodes[1].value
                    },
                    update: function(t) {
                        var e = this.box.childNodes;
                        e[0].childNodes[1].value = w(v(t))
                    }
                };
                var F = function(t, e) {
                    this.btn = c(t, e);
                    var i = this.btn.style;
                    this.btn.innerHTML = e.text,
                    i.font = e.font,
                    i.lineHeight = n(t) * e.height + "px",
                    i.textAlign = "center",
                    i.backgroundColor = e.backgroundColor,
                    i.color = e.color,
                    i.cursor = "pointer"
                }
                  , M = function(t, e) {
                    this.box = c(t, e),
                    this.box.style.backgroundColor = "#000"
                };
                M.prototype = {
                    constructor: M,
                    update: function(t) {
                        for (var e = v(t), i = e.length; i--; )
                            e[i] = (+e[i]).toFixed(0);
                        this.box.style.backgroundColor = "rgb(" + e[0] + ", " + e[1] + ", " + e[2] + ")"
                    }
                };
                var U = function(t) {
                    t = t || {},
                    this.param = e(t, A),
                    this.inited = !1,
                    u.xh5_EvtDispatcher.call(this)
                };
                return U.prototype = {
                    constructor: U,
                    init: function() {
                        if (!this.inited) {
                            var t = this.param
                              , e = N(y(t.color));
                            this._initDoms(t),
                            this._initEvent(),
                            this.update(e),
                            document.body.appendChild(this.wrap),
                            this.inited = !0
                        }
                    },
                    _initDoms: function(t) {
                        var e = document.createElement("div")
                          , i = e.style;
                        i.position = "absolute",
                        i.width = t.width + "px",
                        i.height = t.height + "px",
                        i.zIndex = t.zIndex,
                        i.backgroundColor = t.backgroundColor,
                        i.boxShadow = t.wrapShadow,
                        i.transition = "opacity 0.2s ease-in-out 0s",
                        i.opacity = 0,
                        i.visibility = "hidden",
                        i.userSelect = "none",
                        i.webkitUserSelect = "none",
                        i.msUserSelect = "none",
                        i.mosUserSelect = "none",
                        this.wrap = e,
                        this.picker = new O(e,t.picker),
                        this.slider = new E(e,t.slider),
                        this.rgbBox = new I(e,t.rgbBox),
                        this.hslBox = new L(e,t.hslBox),
                        this.hexBox = new H(e,t.hexBox),
                        this.colorBox = new M(e,t.colorBox),
                        this.okBtn = new F(e,t.okBtn),
                        this.cancelBtn = new F(e,t.cancelBtn)
                    },
                    _initEvent: function() {
                        function t(t) {
                            y = !0,
                            n = +b.left.replace(/[^0-9.]/g, ""),
                            r = +b.top.replace(/[^0-9.]/g, ""),
                            t.targetTouches ? (a = t.targetTouches[0].clientX,
                            o = t.targetTouches[0].clientY) : (a = t.clientX,
                            o = t.clientY)
                        }
                        function e(t) {
                            y && (t.targetTouches ? (s = t.targetTouches[0].clientX - a,
                            l = t.targetTouches[0].clientY - o) : (s = t.clientX - a,
                            l = t.clientY - o),
                            b.left = +n + +s + "px",
                            b.top = +r + +l + "px",
                            T(t)),
                            P(t)
                        }
                        function i() {
                            y = !1
                        }
                        var n, r, a, o, s, l, u = this, c = this.wrap, d = this.picker, h = this.slider, f = this.rgbBox, m = this.hslBox, p = this.hexBox, g = this.okBtn, v = this.cancelBtn, b = c.style, y = !1;
                        "ontouchend"in window ? (k(c, "touchstart", t),
                        k(c, "touchmove", e),
                        k(c, "touchend", i)) : (k(c, "mousedown", t),
                        k(c, "mousemove", e),
                        k(c, "mouseup", i),
                        k(c, "mouseout", i)),
                        d.onmousemove = function() {
                            u.update([d.H, d.S, h.L])
                        }
                        ,
                        h.onmousemove = function() {
                            u.update([d.H, d.S, h.L])
                        }
                        ,
                        m.oninput = function() {
                            u.update(m.getHSLArr())
                        }
                        ,
                        f.oninput = function() {
                            u.update(N(f.getRGBArr()))
                        }
                        ,
                        p.oninput = function() {
                            u.update(p.getHEX())
                        }
                        ,
                        k(g.btn, "click", function() {
                            u.hide(),
                            u.re("ok", [{
                                rgb: f.getRGB(),
                                hsl: m.getHSL(),
                                hex: S(m.getHSL(), "hex")
                            }, u.target]),
                            u.onok && u.onok({
                                rgb: f.getRGB(),
                                hsl: m.getHSL(),
                                hex: S(m.getHSL(), "hex")
                            }, u.target)
                        }),
                        k(v.btn, "click", function() {
                            u.hide()
                        })
                    },
                    show: function(t, e, i, n) {
                        !this.inited && this.init();
                        var r = this.wrap
                          , a = r.style;
                        a.left = (t ? t : 0) + "px",
                        a.top = (e ? e : 0) + "px",
                        a.visibility = "visible",
                        a.opacity = 1,
                        n && this.update(n),
                        this.target = i
                    },
                    hide: function() {
                        if (this.inited) {
                            var t = this.wrap
                              , e = t.style;
                            e.visibility = "hidden",
                            e.opacity = 0
                        }
                    },
                    update: function(t) {
                        var e = "Array" == _(t) ? t : N(y(t));
                        this.picker.update(e),
                        this.slider.update(e),
                        this.rgbBox.update(e),
                        this.hslBox.update(e),
                        this.hexBox.update(e),
                        this.colorBox.update(e)
                    }
                },
                t(U, u.xh5_EvtDispatcher),
                new U
            }
        }(),
        this.HQ_DOMAIN = l(),
        this.MarketTradeTime = v
    }
});
;xh5_define("cfgs.settinger", [], function() {
    "use strict";
    function t(t) {
        this.uid = t,
        this.custom = {
            show_underlay_vol: !0,
            show_ext_marks: !0,
            show_floater: !0,
            mousewheel_zoom: !0,
            keyboard: !0,
            history_t: "window",
            allow_move: !0,
            mouse_and_touch: !0,
            tchart_tap: !0,
            show_k_rangepercent: !0,
            show_k_gap: !0,
            show_k_gap_price: !1,
            k_0pct: "no",
            touch_prevent: !0,
            mini_threshold: {
                width: 0 / 0,
                height: 0 / 0
            },
            show_logo: !0,
            k_overlay: !1,
            stick: !0,
            smooth: !1,
            indicatorpanel_url: "https://current.sina.com.cn/sinatkchart/indicatorpanel.html?20160704",
            allow_indicator_edit: !0,
            storage_lv: 2,
            indicator_reorder: !0,
            indicator_cvs_title: !1,
            indicator_reheight: !1,
            centerZoom: !0,
            show_time_label: "normal"
        },
        this.PARAM = {
            K_CL_NUM: 260,
            updateRate: 5,
            T_RATE: 120,
            minCandleNum: 25,
            maxCandleNum: 0 / 0,
            defaultCandleNum: 64,
            zoomUnit: 90,
            zoomLimit: 10,
            zoomArea: .15,
            I_Z_INDEX: 50,
            G_Z_INDEX: 30,
            _hd: 1,
            setHd: function(t) {
                "number" == typeof t && (this._hd = t)
            },
            getHd: function() {
                return this._hd
            },
            isFlash: !1,
            LOGO_ID: "KKE_sina_finance_logo",
            gapNum: 3
        },
        this.DIMENSION = {
            extend_draw: !1,
            extend_padding: 7,
            LOGO_W: 80,
            LOGO_H: 24,
            posY: 0,
            posX: 55,
            RIGHT_W: 55,
            K_RIGHT_W: 9,
            _w: void 0,
            _h: void 0,
            w_t: void 0,
            w_k: void 0,
            h_t: void 0,
            h_k: void 0,
            P_HV: .28,
            H_MA4K: 13,
            H_TIME_PART: 13,
            K_F_T: 47,
            T_F_T: 13,
            H_T_T: 14,
            W_T_L: 43,
            H_T_G: 60,
            H_BLK: 50,
            H_T_B: 7,
            I_V_O: 0,
            getOneWholeTH: function() {
                return this.H_T_T + this.H_T_G
            },
            H_RS: 30,
            setStageW: function(t) {
                this._w = t,
                this.w_k = t - this.posX - this.K_RIGHT_W,
                this.w_t = t - this.posX - this.RIGHT_W
            },
            setStageH: function(t, e) {
                this._h = t,
                this.h_k = this.h_t = t - e - this.H_TIME_PART - this.H_MA4K
            },
            getStageW: function() {
                return this._w
            },
            getStageH: function() {
                return this._h
            }
        },
        this.STYLE = {
            FONT_SIZE: 12,
            FONT_FAMILY: "helvetica,arial,sans-serif"
        },
        this.COLOR = {
            BG: "#fff",
            T_P: "#007cc8",
            T_AVG: "#000000",
            T_PREV: "#9b9b9b",
            K_RISE: "#f11200",
            K_FALL: "#00a800",
            K_N: "#000000",
            K_CL: "#007cc8",
            K_MS_RISE: "#f11200",
            K_MS_FALL: "#00a800",
            K_MS_N: "#000000",
            K_GAP: "rgba(0,0,0,.1)",
            K_GAP_TXT: "#aaaaaa",
            T_RISE: "#f11200",
            T_FALL: "#00a800",
            T_N: "#000000",
            F_RISE: "#f11200",
            F_FALL: "#00a800",
            F_N: "#000000",
            F_BG: "rgba(255,255,255,.9)",
            F_BR: "#000",
            F_T: "#000",
            K_EXT: "#080208",
            T_T: "#777",
            K_P: "#555",
            V_SD: "#dddddd",
            M_ARR: ["#fff", "#BCD4F9"],
            M_ARR_A: [.5, 0],
            TIME_S: "#000000",
            TIME_L: "#eeeeee",
            GRID: "#eee",
            IVH_LINE: "#494949",
            P_TC: "#fff",
            P_BG: "#494949",
            T_TC: "#fff",
            T_BG: "#494949",
            REMARK_T: "#fff",
            REMARK_BG: "#494949",
            K_PCT: "#ccc",
            BTN_ARR: ["#2b9dfc", "#fff"],
            TIP_ARR: ["#000", "#fff", null, !1, null],
            LOGO: "#ccc"
        },
        this.datas = {
            s: "sh000001",
            mode: "",
            tDataLen: 241,
            t: "",
            isT: !1,
            scaleType: "price",
            candle: "solid"
        }
    }
    var e = {
        URLHASH: {
            TS: 1,
            T1: 1,
            T5: 5,
            FAKE_T5: 2,
            NTS: "ts",
            NT5: "t5",
            KD: 24,
            KW: 168,
            KM: 720,
            KCL: 365,
            KY: 8760,
            KDF: 23,
            KDB: 25,
            KWF: 167,
            KWB: 169,
            KMF: 719,
            KMB: 721,
            KCLF: 364,
            KCLB: 366,
            KYF: 8759,
            KYB: 8761,
            NKD: "kd",
            NKW: "kw",
            NKM: "km",
            NKCL: "kcl",
            NKY: "ky",
            NKYF: "kyf",
            NKYB: "kyb",
            NKDF: "kdf",
            NKDB: "kdb",
            NKWF: "kwf",
            NKWB: "kwb",
            NKMF: "kmf",
            NKMB: "kmb",
            NKCLF: "kclf",
            NKCLB: "kclb",
            K1: 1,
            K5: 5,
            K15: 15,
            K30: 30,
            K60: 60,
            K240: 240,
            NK1: "k1",
            NK5: "k5",
            NK15: "k15",
            NK30: "k30",
            NK60: "k60",
            NK240: "k240",
            KMS: 1e3,
            NKMS: "kms",
            KYTD: 983,
            NYTD: "kytd",
            vn: function(t) {
                for (var e in this)
                    if (this.hasOwnProperty(e) && "number" == typeof this[e] && t == this[e])
                        return this[e];
                return void 0
            },
            vi: function(t) {
                switch (t) {
                case this.NTS:
                    return this.TS;
                case this.NT5:
                    return this.FAKE_T5;
                default:
                    return this[t.toUpperCase()]
                }
            },
            gt: function(t) {
                var e;
                switch (t) {
                case this.KMS:
                    e = {
                        type: "msk"
                    };
                    break;
                case this.K1:
                case this.K5:
                case this.K15:
                case this.K30:
                case this.K60:
                case this.K240:
                    e = {
                        type: "mink"
                    };
                    break;
                case this.KDF:
                case this.KWF:
                case this.KMF:
                case this.KYF:
                case this.KCLF:
                    e = {
                        type: "rek",
                        dir: "q"
                    };
                    break;
                case this.KDB:
                case this.KWB:
                case this.KMB:
                case this.KYB:
                case this.KCLB:
                    e = {
                        type: "rek",
                        dir: "h"
                    };
                    break;
                default:
                    e = {
                        type: "k"
                    }
                }
                switch (t) {
                case this.KD:
                case this.KDF:
                case this.KDB:
                    e.baseid = this.KD;
                    break;
                case this.KW:
                case this.KWF:
                case this.KWB:
                    e.baseid = this.KW;
                    break;
                case this.KM:
                case this.KMF:
                case this.KMB:
                    e.baseid = this.KM;
                    break;
                case this.KY:
                case this.KYF:
                case this.KYB:
                    e.baseid = this.KY;
                    break;
                case this.KCL:
                case this.KCLF:
                case this.KCLB:
                    e.baseid = this.KCL;
                    break;
                default:
                    e.baseid = t
                }
                return e
            }
        },
        e: {
            K_DATA_LOADED: "kDataLoaded",
            T_DATA_LOADED: "tDataLoaded",
            I_EVT: "iEvent"
        },
        nohtml5info: "\u68c0\u6d4b\u5230\u60a8\u7684\u6d4f\u89c8\u5668\u8fc7\u65e7\u4e14\u4e0d\u652f\u6301HTML 5\uff0c\u5f53\u524d\u4ee5\u517c\u5bb9\u6a21\u5f0f\u8fd0\u884c\u3002<br/>\u4e3a\u83b7\u5f97\u66f4\u597d\u7684\u4f53\u9a8c\u53ca\u5b8c\u5584\u7684\u529f\u80fd\uff0c\u5efa\u8bae\u4f7f\u7528<a style='color:#fff;text-decoration:underline;' href='http://down.tech.sina.com.cn/content/40975.html' target='_blank'>\u8c37\u6b4cChrome</a>\u6d4f\u89c8\u5668\uff0c\u6216\u5347\u7ea7\u5230\u60a8\u6d4f\u89c8\u5668\u7684<a style='color:#fff;text-decoration:underline;' href='http://down.tech.sina.com.cn/content/58979.html' target='_blank'>\u6700\u65b0\u7248\u672c</a>\u3002",
        historyt08: "\u5f53\u524d\u63d0\u4f9bA\u80a12008\u5e74\u4ee5\u6765\u7684\u5386\u53f2\u5206\u65f6\u8d70\u52bf\u67e5\u8be2",
        nohistoryt: "\u65e0\u6b64\u8bc1\u5238\u6b64\u65f6\u6bb5\u5386\u53f2\u5206\u65f6\u6570\u636e",
        norecord: "\u8bc1\u5238\u4ee3\u7801\u65e0\u8bb0\u5f55",
        notlisted: "\u672a\u4e0a\u5e02",
        delisted: "\u9000\u5e02",
        nodata: "\u672a\u52a0\u8f7d\u5230\u6709\u6548\u6570\u636e",
        noredata: "\u90e8\u5206\u8bc1\u5238\u65e0\u590d\u6743\u6570\u636e"
    };
    return new function() {
        this.VER = "2.1.2";
        var n = [];
        this.getSetting = function(e) {
            for (var i, s = n.length; s--; )
                if (i = n[s],
                e == i.uid)
                    return i;
            return i = new t(e),
            n.push(i),
            i
        }
        ,
        this.globalCfg = e
    }
});
;xh5_define("datas.hq", ["utils.util"], function(e) {
    "use strict";
    var t = e.load
      , i = e.fBind
      , a = e.market
      , r = e.cookieUtil
      , n = e.dateUtil
      , s = e.tUtil
      , o = 0 == location.protocol.indexOf("https:")
      , l = e.HQ_DOMAIN
      , u = e.MarketTradeTime
      , m = new function() {
        var e, i = "sinaH5EtagStatus", a = {
            domain: "",
            path: "/",
            expires: 3600
        }, n = "n", s = "y", u = 0, m = (o ? "https" : "http") + "://" + l + ".sinajs.cn/list=sys_hqEtagMode", d = function() {
            t(m, function() {
                var t = window.hq_str_sys_hqEtagMode;
                0 == u ? u = t : (u == t ? (e = !1,
                r.set(i, n, a)) : (e = !0,
                r.set(i, s, a)),
                u = 0)
            })
        }, h = function() {
            var t = r.get(i);
            switch (t) {
            case n:
                e = !1;
                break;
            case s:
                e = !0;
                break;
            default:
                e = !1,
                d()
            }
        };
        h(),
        setInterval(h, 2e3),
        this.isETag = function() {
            return e
        }
    }
      , d = function(e, t) {
        if (e.length > 1) {
            for (var i = 0; i < e.length - 1; i++)
                if (e[i][1] > e[i + 1][0]) {
                    if (t > e[i][1])
                        return e[i][1];
                    if (t < e[i + 1][0])
                        return e[i][1]
                } else if (t > e[i][1] && t < e[i + 1][0])
                    return e[i][1];
            return e[e.length - 1][1]
        }
        return e[e.length - 1][1]
    }
      , h = function() {
        function r(t, i, a) {
            var r = {}
              , n = g[t];
            n || (n = {
                symbol: t
            },
            g[t] = n);
            var s = x.trHandler(a, n);
            s && (n.trstr = a),
            r[t] = n;
            var o = {
                msg: "",
                dataObj: r
            };
            return e.isFunc(i) && i(o),
            o
        }
        function h(t, i, r, n) {
            if (n && --n.count > 0)
                return null;
            for (var s, o, l, u, m, d, h, c = t.split(","), f = [], p = {}, b = 0, g = c.length; g > b; b++) {
                s = c[b],
                l = N[s],
                l || (l = {
                    symbol: s
                },
                N[s] = l),
                o = a(s);
                var v = 0;
                if (r)
                    u = r;
                else
                    switch (u = window["hq_str_" + s],
                    o) {
                    case "HK":
                        m = window["hq_str_" + s.replace("rt_", "") + "_i"],
                        h = window.hq_str_rt_hkHSI;
                        break;
                    case "US":
                        h = window.hq_str_gb_$ixic || window.hq_str_gb_ixic || window.hq_str_gb_$dji || window.hq_str_gb_dji;
                        break;
                    case "NF":
                        m = window["hq_str_" + s + "_i"],
                        m && (v = "cffex" == m.split(",")[3]);
                        break;
                    default:
                        m = window["hq_str_" + s + "_i"]
                    }
                d = u && u.length > 0 ? u.split(",") : void 0;
                var _;
                switch (o) {
                case "REPO":
                    _ = k;
                    break;
                case "SI":
                    _ = T;
                    break;
                case "CN":
                    _ = x;
                    break;
                case "CNI":
                    _ = x;
                    break;
                case "US":
                    _ = D;
                    break;
                case "HKAP":
                    _ = E;
                    break;
                case "HK":
                    _ = R;
                    break;
                case "OTC":
                    _ = H;
                    break;
                case "HF":
                    _ = F;
                    break;
                case "GOODS":
                    _ = L;
                    break;
                case "NF":
                    _ = v ? P : I;
                    break;
                case "global_index":
                    _ = A;
                    break;
                case "fund":
                    _ = K;
                    break;
                case "op_m":
                case "option_cn":
                    _ = U;
                    break;
                case "forex":
                case "forex_yt":
                    _ = y;
                    break;
                case "CFF":
                    _ = P;
                    break;
                case "BTC":
                    _ = w;
                    break;
                case "MSCI":
                    _ = O;
                    break;
                case "LSE":
                    _ = M;
                    break;
                case "globalbd":
                    _ = C;
                    break;
                default:
                    _ = void 0
                }
                var S = !0;
                _ && (S = _.update(d, l, m, h)),
                S && (l.hqstr = u),
                f.push(l),
                p[s] = l
            }
            var B = {
                msg: "",
                data: f,
                dataObj: p
            };
            return e.isFunc(i) && i(B),
            B
        }
        function c(t) {
            var i = 40
              , a = t.split(",")
              , r = [];
            for (a = e.uae(a); a.length > i; )
                r.push(a.splice(0, i));
            return r.push(a.splice(0, a.length)),
            r
        }
        this.VER = "2.9.0";
        var f, p = {
            "00": "",
            "01": "\u505c\u724c\u4e00\u5c0f\u65f6",
            "02": "\u505c\u724c\u4e00\u5929",
            "03": "\u8fde\u7eed\u505c\u724c",
            "04": "\u76d8\u4e2d\u505c\u724c",
            "05": "\u505c\u724c\u534a\u5929",
            "06": "\u505c\u724c\u534a\u5c0f\u65f6",
            "07": "\u6682\u505c",
            "08": "\u53ef\u6062\u590d\u4ea4\u6613\u7194\u65ad",
            "09": "\u4e0d\u53ef\u6062\u590d\u4ea4\u6613\u7194\u65ad"
        }, b = (new Date).getTime(), N = {}, g = {}, v = new function() {
            var e = l + ".sinajs.cn"
              , i = "://" + e + "/?_=$rn&list=$symbol"
              , a = "://" + e + "/etag.php?_=" + b + "&list=$symbol"
              , r = function(e) {
                var t, r = o ? "https" : e.ssl ? "https" : "http";
                return t = e.cancelEtag ? r + i.replace("$rn", String(Math.random())) : r + (m.isETag() ? a : i.replace("$rn", String(Math.random())))
            };
            return function(e, i, a) {
                a = a || {},
                t(r(a).replace("$symbol", e), i)
            }
        }
        , _ = function(e) {
            var t = e.timeStr || ""
              , i = e.dateStr || ""
              , a = e.tArr || void 0
              , r = e.hqObj || {}
              , o = e.dateDiv || "-"
              , l = t.split(":")
              , u = Number(l[0]) || 0
              , m = Number(l[1]) || 0
              , d = Number(l[2]) || 0
              , h = 0 / 0
              , c = [s.s0(u), s.s0(m)].join(":");
            if (a) {
                if (a.indexOf)
                    h = a.indexOf(c);
                else
                    for (var f = a.length; f--; )
                        if (a[f] == c) {
                            h = f;
                            break
                        }
                e.market && "CN" == e.market && (11 == u && m > 29 || u >= 15 && a[a.length - 1] < t || (h++,
                [u,m] = a[h].split(":")))
            }
            c = [s.s0(u), s.s0(m)].join(":");
            var p = {
                time: c,
                isUpdateTime: isNaN(h) ? !0 : Boolean(h >= 0),
                index: h
            }
              , b = i.split(o)
              , N = ~~Number(b[0])
              , g = ~~(Number(b[1]) - 1)
              , v = ~~Number(b[2])
              , _ = {
                isErrData: !1,
                isDateChange: !1,
                date: r.date,
                today: [N, g + 1, v].join("-")
            };
            if (r.date) {
                var S = new Date(N,g,v,u,m,d)
                  , w = n.stbd(r.date, S);
                w ? S >= r.date ? _.date.setHours(u, m, d) : _.isErrData = !0 : (_.isDateChange = Boolean(S > r.date),
                _.isDateChange ? _.date = S : _.isErrData = !0)
            } else
                i ? _.date = new Date(N,g,v,u,m,d) : _.isErrData = !0;
            return {
                datePart: _,
                timePart: p
            }
        }, S = {
            swap: function(e) {
                var t, i = e.split(","), a = "";
                i[8] = "TP" == i[8] ? "03" : "00",
                t = [0, 4, 3, 7, 5, 6, 26, 46, 10, 11, 36, 26, 37, 27, 38, 28, 39, 29, 40, 30, 56, 46, 57, 47, 58, 48, 59, 49, 60, 50, 2, 1, 8];
                for (var r = 0; r < t.length; r++)
                    a += i[t[r]] + ",";
                return a = a.slice(0, a.length - 1)
            },
            kak: function(e, t) {
                var i;
                switch (t) {
                case "CN_2":
                    i = this.swap(e);
                    break;
                default:
                    i = e
                }
                return i
            }
        }, w = new function() {
            var e;
            this.update = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gtr([["0:00", "23:59"]]));
                var a = e
                  , r = "00:00"
                  , n = t[11]
                  , o = t[0]
                  , l = _({
                    dateStr: n,
                    timeStr: o,
                    hqObj: i,
                    tArr: a,
                    start: r
                });
                if (l.datePart.isErrData)
                    return !1;
                i.date = l.datePart.date,
                i.today = l.datePart.today,
                i.time = l.timePart.time,
                i.index = l.timePart.index,
                i.isUpdateTime = l.timePart.isUpdateTime,
                i.name = String(t[9]);
                var u = Number(t[3]) || 0;
                return i.prevclose = u,
                i.open = Number(t[5]) || u,
                i.high = Number(t[6]) || u,
                i.low = Number(t[7]) || u,
                i.price = Number(t[8]) || u,
                i.totalVolume = 0,
                !0
            }
        }
        , y = new function() {
            var e, t;
            this.update = function(i, a) {
                if (!i)
                    return !1;
                e || (e = s.gtr([["6:00", "23:59"], ["0:00", "5:59"]]));
                var r = e
                  , n = "06:00"
                  , o = 17
                  , l = a.symbol;
                0 !== l.indexOf("fx_") && (o = 10,
                "DINIW" == l && (t || (t = s.gtr([["6:00", "23:59"], ["0:00", "5:59"]])),
                r = t,
                n = "06:00"));
                var u = i[o]
                  , m = i[0]
                  , d = _({
                    dateStr: u,
                    timeStr: m,
                    hqObj: a,
                    tArr: r,
                    start: n
                });
                if (d.datePart.isErrData)
                    return !1;
                a.date = d.datePart.date,
                a.today = d.datePart.today,
                a.time = d.timePart.time,
                a.index = d.timePart.index,
                a.isUpdateTime = d.timePart.isUpdateTime,
                a.name = String(i[9]);
                var h = Number(i[3]) || 0;
                return a.prevclose = h,
                a.open = Number(i[5]) || h,
                a.high = Number(i[6]) || h,
                a.low = Number(i[7]) || h,
                a.price = Number(i[8]) || h,
                a.totalVolume = 0,
                !0
            }
        }
        , T = new function() {
            var t, i, a = function(i, a) {
                if (!i)
                    return !1;
                t || (t = e.isRepos(a.symbol) ? s.gtrepo() : s.gta());
                var r = i[30]
                  , n = i[31]
                  , o = _({
                    dateStr: r,
                    timeStr: n,
                    hqObj: a,
                    tArr: t,
                    start: "09:30"
                });
                if (o.datePart.isErrData)
                    return !1;
                if (a.date = o.datePart.date,
                a.isDateChange = o.datePart.isDateChange,
                a.today = o.datePart.today,
                a.time = o.timePart.time,
                a.index = o.timePart.index,
                a.index < 0 && a.time > "09:29" && (a.time = d(u.CN, a.time),
                a.index = t.indexOf(a.time)),
                a.isUpdateTime = o.timePart.isUpdateTime,
                !o.timePart.isUpdateTime) {
                    var l, m, h = a.time.split(":"), c = Number(h[0]), f = Number(h[1]);
                    switch (c) {
                    case 11:
                        36 > f && (a.isUpdateTime = !0,
                        a.index = 120);
                        break;
                    case 15:
                        e.isRepos(a.symbol) ? (l = 40,
                        m = 270) : (l = 40,
                        m = 240),
                        l > f && (a.isUpdateTime = !0,
                        a.index = m)
                    }
                }
                a.name = String(i[0]),
                a.isNewListed = Boolean(0 == a.name.indexOf("N"));
                var b = Number(i[2]) || 0;
                a.prevclose = b,
                a.preopen = Number(i[1]) || Number(i[6]) || Number(i[7]) || b,
                a.open = Number(i[1]) || b,
                a.price = Number(i[3]) || b,
                a.high = Number(i[4]) || b,
                a.low = Number(i[5]) || b,
                a.buy = Number(i[6]),
                a.sell = Number(i[7]);
                var N = Number(i[8]) || 0;
                N /= 1,
                a.totalVolume = N,
                a.totalAmount = Number(i[9]) || 0;
                var g = i.length >= 34 ? i[33].split("|") : [];
                a.isKCBF = g.length > 0,
                a.isKCBF && (a.KCBState = g[0],
                a.postVolume = Number(g[1]) || 0,
                a.postAmount = Number(g[2]) || 0,
                a.postVolume = a.postVolume / 100);
                var v = i[32];
                return a.state = v,
                a.isStopDay = "02" == v || "03" == v,
                a.statusStr = p[v] || "",
                !0
            }, r = function(e, t) {
                var i = e.split(",");
                if (i && !(i.length < 16)) {
                    t.type = String(i[0]).toLowerCase(),
                    t.lastfive = Number(i[6]),
                    t.fc = Number(i[8]),
                    t.issueprice = Number(i[14]),
                    t.status = Number(i[15]);
                    var a = i[23].split("|");
                    t.isKCB = "K" === a[0] || "KC" === a[0],
                    t.isCYB = "G" === a[0] || "GC" === a[0],
                    t.KCBType = a[0],
                    t.issuedCapital = Number(a[4]),
                    t.totalRegisteredCapital = Number(a[3]),
                    t.minimumPrice = a[2],
                    t.sameShareAndRight = a[1]
                }
            }, o = function(t, a) {
                i || (i = s.gtr([["9:15", "11:30"], ["13:00", "15:01"]]));
                var r = N[a.symbol] || {}
                  , o = r.date;
                e.isDate(o) || (o = new Date);
                var l = t.split("|")
                  , u = n.ds(o)
                  , m = l[1]
                  , d = _({
                    dateStr: u,
                    timeStr: m,
                    hqObj: a,
                    tArr: i,
                    start: "09:15"
                });
                return d.datePart.isErrData ? !1 : d.datePart.date.getHours() - o.getHours() > 2 ? !1 : (a.date = d.datePart.date,
                a.isDateChange = d.datePart.isDateChange,
                a.today = d.datePart.today,
                a.time = d.timePart.time,
                a.index = d.timePart.index,
                a.isUpdateTime = d.timePart.isUpdateTime,
                a.name = r.name || "",
                a.isNewListed = Boolean(0 == a.name.indexOf("N")),
                a.price = Number(l[2]),
                a.trvolume = .01 * (Number(l[3]) || 0),
                a.tramount = Number(l[4]) || 0,
                a.trbs = Number(l[7]) || 0,
                !0)
            };
            this.trHandler = function(e, t) {
                return o(e, t)
            }
            ,
            this.update = function(e, t, i) {
                var n = !0;
                return i && r(i, t),
                e && (n = a(e, t)),
                n
            }
        }
        , x = new function() {
            var t, i, a = function(i, a) {
                if (!i)
                    return !1;
                t || (t = "z" == a.type ? "BDC" == a.stockSubType ? s.gta() : s.gtrepo() : e.isLongtime(a.symbol) ? s.gtrepo() : e.isRepos(a.symbol) ? s.gtrepo() : s.gta());
                var r = 100;
                /[gz]/i.test(a.type) ? r = 10 : (/^(sh000|sh580)\d+/.test(a.symbol) || /^(hy|gn|dy)\d+/.test(a.symbol)) && (r = 1),
                e.isCNK(a.symbol) && (r = 100);
                var n = i[30]
                  , o = i[31]
                  , l = _({
                    dateStr: n,
                    timeStr: o,
                    hqObj: a,
                    tArr: t,
                    start: "09:30",
                    market: "CN"
                });
                if (l.datePart.isErrData)
                    return !1;
                if (a.date = l.datePart.date,
                a.isDateChange = l.datePart.isDateChange,
                a.today = l.datePart.today,
                a.time = l.timePart.time,
                console.log(" hq \u5904\u7406\u884c\u60c5\u65f6\u95f4:", a.time),
                a.index = l.timePart.index,
                a.index < 0 && a.time > "09:29" && (a.time = d(u.CN, a.time),
                a.index = t.indexOf(a.time)),
                a.isUpdateTime = l.timePart.isUpdateTime,
                !l.timePart.isUpdateTime) {
                    var m, h, c = a.time.split(":"), f = Number(c[0]), b = Number(c[1]);
                    switch (f) {
                    case 11:
                        36 > b && (a.isUpdateTime = !0,
                        a.index = 120);
                        break;
                    case 15:
                        e.isRepos(a.symbol) ? (m = 40,
                        h = 270) : "z" == a.type ? "BDC" == a.stockSubType ? (m = 40,
                        h = 240) : (m = 40,
                        h = 270) : (m = 40,
                        h = 240),
                        m > b && (a.isUpdateTime = !0,
                        a.index = h)
                    }
                }
                a.name = String(i[0]),
                a.isNewListed = Boolean(0 == a.name.indexOf("N"));
                var N = Number(i[2]) || 0;
                a.prevclose = N,
                a.preopen = Number(i[1]) || Number(i[6]) || Number(i[7]) || N,
                a.open = Number(i[1]) || N,
                a.price = Number(i[3]) || N,
                a.high = Number(i[4]) || N,
                a.low = Number(i[5]) || N,
                a.buy = Number(i[6]),
                a.sell = Number(i[7]);
                var g = Number(i[8]) || 0;
                g /= r,
                a.totalVolume = g,
                a.totalAmount = Number(i[9]) || 0;
                var v = i.length >= 34 ? i[33].split("|") : [];
                a.isKCBF = v.length > 0,
                a.isKCBF && (a.KCBState = v[0],
                a.postVolume = Number(v[1]) || 0,
                a.postAmount = Number(v[2]) || 0,
                a.postVolume = a.postVolume / 100);
                var S = i[32];
                return a.state = S,
                a.isStopDay = "02" == S || "03" == S,
                a.statusStr = p[S] || "",
                !0
            }, r = function(e, t) {
                var i = e.split(",");
                if (i && !(i.length < 16)) {
                    t.type = String(i[0]).toLowerCase(),
                    t.lastfive = Number(i[6]),
                    t.fc = Number(i[8]),
                    t.issueprice = Number(i[14]),
                    t.status = Number(i[15]);
                    var a = i[23].split("|");
                    t.isKCB = "K" === a[0] || "KC" === a[0],
                    t.isCYB = "G" === a[0] || "GC" === a[0],
                    t.KCBType = a[0],
                    t.issuedCapital = Number(a[4]),
                    t.totalRegisteredCapital = Number(a[3]),
                    t.minimumPrice = a[2],
                    t.sameShareAndRight = a[1],
                    t.stockSubType = i[30]
                }
            }, o = function(t, a) {
                i || (i = s.gtr([["9:15", "11:30"], ["13:00", "15:01"]]));
                var r = N[a.symbol] || {}
                  , o = r.date;
                e.isDate(o) || (o = new Date);
                var l = t.split("|")
                  , u = n.ds(o)
                  , m = l[1]
                  , d = _({
                    dateStr: u,
                    timeStr: m,
                    hqObj: a,
                    tArr: i,
                    start: "09:15"
                });
                return d.datePart.isErrData ? !1 : d.datePart.date.getHours() - o.getHours() > 2 ? !1 : (a.date = d.datePart.date,
                a.isDateChange = d.datePart.isDateChange,
                a.today = d.datePart.today,
                a.time = d.timePart.time,
                a.index = d.timePart.index,
                a.isUpdateTime = d.timePart.isUpdateTime,
                a.name = r.name || "",
                a.isNewListed = Boolean(0 == a.name.indexOf("N")),
                a.price = Number(l[2]),
                a.trvolume = .01 * (Number(l[3]) || 0),
                a.tramount = Number(l[4]) || 0,
                a.trbs = Number(l[7]) || 0,
                !0)
            };
            this.trHandler = function(e, t) {
                return o(e, t)
            }
            ,
            this.update = function(e, t, i) {
                var n = !0;
                return i && r(i, t),
                e && (n = a(e, t)),
                n
            }
        }
        , k = e.clone(x), P = new function() {
            var e;
            this.update = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gata(a(i.symbol), window["kke_future_" + i.symbol] && window["kke_future_" + i.symbol].time || [["09:30", "11:29"], ["13:00", "02:59"]]));
                var r = t[36]
                  , n = t[37]
                  , o = _({
                    dateStr: r,
                    timeStr: n,
                    hqObj: i,
                    tArr: e,
                    start: e[0]
                });
                if (o.datePart.isErrData)
                    return !1;
                i.name = t[49] || i.symbol.replace("CFF_RE_", ""),
                i.date = o.datePart.date,
                i.isDateChange = o.datePart.isDateChange,
                i.today = o.datePart.today,
                i.time = o.timePart.time,
                i.index = o.timePart.index,
                i.isUpdateTime = o.timePart.isUpdateTime;
                var l = Number(t[14]) || Number(t[13]) || Number(t[0]) || 0;
                return i.settlement = i.prevclose = l,
                i.open = Number(t[0]) || l,
                i.price = Number(t[3]) || l,
                i.high = Number(t[1]) || l,
                i.low = Number(t[2]) || l,
                i.preopen = i.open,
                i.totalVolume = Number(t[4]) || 0,
                i.totalAmount = Number(t[5]) || 0,
                i.holdingAmount = Number(t[6]) || 0,
                i.preHoldingAmount = Number(t[15]) || 0,
                i.iscff = 1,
                i.withNight = !1,
                !0
            }
        }
        , D = new function() {
            var t, i = function(t) {
                if (!t || t.length < 9)
                    return null;
                for (var i, a = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], r = t.split(" "), n = new Date, s = n.getFullYear(), o = 0, l = a.length; l > o; o++)
                    if (String(r[0]).toUpperCase() == String(a[o]).toUpperCase()) {
                        i = o;
                        break
                    }
                var u = parseInt(Number(r[1]))
                  , m = String(r[2])
                  , d = m.toUpperCase().indexOf("PM") > 0
                  , h = m.split(":")
                  , c = parseInt(Number(h[0]));
                d && 12 != c && (c += 12);
                var f = h[1]
                  , p = f.slice(0, -2)
                  , b = [e.strUtil.zp(c), e.strUtil.zp(p), "00"].join(":")
                  , N = new Date(s,i,u);
                if (+N > +n) {
                    if (!(0 == n.getMonth() && n.getDate() < 7))
                        return null;
                    s--,
                    N = new Date(s,i,u)
                }
                var g = [N.getFullYear(), e.strUtil.zp(N.getMonth() + 1), e.strUtil.zp(N.getDate())].join("-");
                return [b, g]
            }, a = function(e, t) {
                if (e && t) {
                    var i = e.split(",");
                    !i || i.length < 3 || (t.exchange = i[0],
                    t.industry = i[1],
                    t.issueprice = i[2])
                }
            }, r = function(e, a, r) {
                function o(e) {
                    return 0 === parseInt(e[2]) && 0 === parseInt(e[4]) && 0 === parseInt(e[5]) && 0 === parseInt(e[6]) && 0 === parseInt(e[7]) && 0 === parseInt(e[10])
                }
                if (!e || e.length < 28)
                    return !1;
                t || (t = s.gtus());
                var l, m = !1;
                r ? (l = r.split(","),
                m = o(l)) : m = o(e);
                var h;
                if (a.prevclose = Number(e[26]) || Number(e[1]) || 0,
                m) {
                    a.high = a.prevclose,
                    a.open = a.prevclose,
                    a.low = a.prevclose;
                    var c = new Date((window.hq_str_sys_time ? new Date(1e3 * window.hq_str_sys_time) : new Date) - 432e5);
                    h = ["09:10", c.getFullYear() + "-" + (c.getMonth() + 1) + "-" + c.getDate()]
                } else
                    a.open = Number(e[5]) || a.prevclose,
                    a.high = Number(e[6]) || a.prevclose,
                    a.low = Number(e[7]) || a.prevclose,
                    h = i(String(l ? l[25] : e[25]));
                if (a.name = e[0],
                a.price = Number(e[1]) || a.open,
                a.preopen = a.open,
                a.totalVolume = Number(e[10]) || 0,
                a.isUnlisted = 0 == a.price && 0 == Number(e[8]) && 0 == Number(e[9]),
                h) {
                    var f = _({
                        dateStr: h[1],
                        timeStr: h[0],
                        hqObj: a,
                        tArr: t
                    });
                    a.date = f.datePart.date,
                    a.isDateChange = f.datePart.isDateChange,
                    a.today = f.datePart.today,
                    a.time = f.timePart.time,
                    a.index = f.timePart.index,
                    a.index < 0 && a.time > "09:30" && (a.time = d(u.US, a.time),
                    a.index = t.indexOf(a.time)),
                    a.isUpdateTime = f.timePart.isUpdateTime,
                    n = !0
                }
                return !0
            }, n = !1;
            this.update = function(e, t, i, n) {
                var s;
                return i && a(i, t),
                e && (s = r(e, t, n)),
                s
            }
        }
        , O = new function() {
            var e;
            this.update = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gtmsci());
                var a = n.dss(new Date(1 * t[6]), "-").split(" ")
                  , r = a[0]
                  , o = a[1]
                  , l = "07:00"
                  , u = _({
                    dateStr: r,
                    dateDiv: "-",
                    timeStr: o,
                    hqObj: i,
                    tArr: e,
                    start: l
                });
                i.date = u.datePart.date,
                i.isDateChange = u.datePart.isDateChange,
                i.today = u.datePart.today,
                i.time = u.timePart.time,
                i.index = u.timePart.index,
                i.isUpdateTime = u.timePart.isUpdateTime,
                i.name = t[1];
                var m = Number(t[22]) || 0;
                return i.prevclose = m,
                i.open = Number(t[21]) || m,
                i.preopen = i.open,
                i.high = Number(t[19]) || m,
                i.low = Number(t[20]) || m,
                i.price = Number(t[4]) || m,
                i.totalVolume = 0,
                i.totalAmount = 0,
                !0
            }
        }
        , C = new function() {
            var e, t = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gtglobaldb());
                var a = t[12]
                  , r = t[13]
                  , o = "08:00";
                a || (a = n.ds(new Date),
                r = o);
                var l = _({
                    dateStr: a,
                    dateDiv: "-",
                    timeStr: r,
                    hqObj: i,
                    tArr: e,
                    start: "08:00"
                });
                i.date = l.datePart.date,
                i.isDateChange = l.datePart.isDateChange,
                i.today = l.datePart.today,
                i.time = l.timePart.time,
                i.index = l.timePart.index,
                i.index < 0 && (i.time = d(u.globalbd, i.time),
                i.index = e.indexOf(i.time)),
                i.isUpdateTime = !0,
                i.name = t[0];
                var m = Number(t[2]) || 0;
                return i.prevclose = m,
                i.open = Number(t[1]) || m,
                i.preopen = i.open,
                i.price = Number(t[3]) || m,
                i.high = Number(t[4]) || m,
                i.low = Number(t[5]) || m,
                i.high52 = Number(t[9]),
                i.low52 = Number(t[10]),
                !0
            };
            this.update = function(e, i, a) {
                var r;
                return e && (r = t(e, i, a)),
                r
            }
        }
        , M = new function() {
            var e, t = function(t, i, a) {
                if (!t)
                    return !1;
                e || (e = s.gtlse());
                var r = t[8].split(" ")
                  , o = a && a.split(",") || []
                  , l = r[0]
                  , m = r[1]
                  , h = "08:00";
                l || (l = n.ds(new Date),
                m = h),
                h > m && (m = h);
                var c = _({
                    dateStr: l,
                    dateDiv: "-",
                    timeStr: m,
                    hqObj: i,
                    tArr: e,
                    start: "08:00"
                });
                i.date = c.datePart.date,
                i.isDateChange = c.datePart.isDateChange,
                i.today = c.datePart.today,
                i.time = c.timePart.time,
                i.index = c.timePart.index,
                i.index < 0 && (i.time = d(u.LSE, i.time),
                i.index = e.indexOf(i.time)),
                i.isUpdateTime = c.timePart.isUpdateTime,
                i.name = o[0] || o[1] || String(t[0]);
                var f = Number(t[5]) || 0;
                return o.length > 6 && o[5] && (i.issueprice = Number(o[5]),
                n.stbd(n.sd(o[6]), i.date) && (f = i.issueprice)),
                i.prevclose = f,
                i.open = Number(t[3]) || f,
                i.preopen = i.open || i.price,
                i.high = Number(t[2]) || f,
                i.low = Number(t[4]) || f,
                i.buy = Number(t[9]),
                i.sell = Number(t[11]),
                i.price = Number(t[1]) || f,
                i.totalVolume = Number(t[6]) || 0,
                i.totalAmount = Number(t[7]) || 0,
                i.state = t[13],
                i.stateUpdate = t[14],
                i.stateTimeStart = t[15],
                i.stateTimeEnd = t[16],
                i.dataSource = t[17],
                !0
            };
            this.update = function(e, i, a) {
                var r;
                return e && (r = t(e, i, a)),
                r
            }
        }
        , K = new function() {
            var e;
            this.update = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gta());
                var a = t[7]
                  , r = t[1]
                  , n = _({
                    dateStr: a,
                    dateDiv: "-",
                    timeStr: r,
                    hqObj: i,
                    tArr: e,
                    start: "09:30"
                });
                return i.date = n.datePart.date,
                i.isDateChange = n.datePart.isDateChange,
                i.today = n.datePart.today,
                i.time = n.timePart.time,
                i.index = n.timePart.index,
                i.index < 0 && (i.time = d(u.CN, i.time),
                i.index = e.indexOf(i.time)),
                i.isUpdateTime = n.timePart.isUpdateTime,
                i.name = String(t[0]),
                i.volume = 0,
                i.price = Number(t[2]),
                i.prevprice = i.prevclose = Number(t[3]),
                !0
            }
        }
        , I = new function() {
            this.update = function(e, t) {
                if (!e)
                    return !1;
                var i = window["kke_future_" + t.symbol] && window["kke_future_" + t.symbol].time || [["09:30", "11:29"], ["13:00", "02:59"]]
                  , r = s.gata(a(t.symbol), i)
                  , n = e[1]
                  , o = e[17]
                  , l = n.slice(0, 2) + ":" + n.slice(2, 4)
                  , u = _({
                    dateStr: o,
                    dateDiv: "-",
                    timeStr: l,
                    hqObj: t,
                    tArr: r,
                    start: r[0]
                });
                t.date = u.datePart.date,
                t.isDateChange = u.datePart.isDateChange,
                t.today = u.datePart.today,
                t.time = u.timePart.time,
                t.index = u.timePart.index,
                t.isUpdateTime = u.timePart.isUpdateTime,
                u.timePart.index < 0 && (t.time = d(i, t.time),
                t.index = r.indexOf(t.time)),
                r[0] > "15:00" && ("00:00" == i[1][0] ? l > i[1][1] && "09:00" > l && (t.index = r.indexOf(i[1][1])) : l > i[0][1] && "09:00" > l && (t.index = r.indexOf(i[0][1]))),
                t.name = String(e[0]);
                var m = Number(e[10]) || 0;
                return t.prevclose = m,
                t.open = Number(e[2]) || m,
                t.preopen = t.open || t.price,
                t.high = Number(e[3]) || m,
                t.low = Number(e[4]) || m,
                t.close = Number(e[5]) || m,
                t.buy = Number(e[6]),
                t.sell = Number(e[7]),
                t.price = Number(e[8]) || m,
                t.activeprevclose = Number(e[9]),
                t.buyAmount = Number(e[11]),
                t.sellAmount = Number(e[12]),
                t.holdingAmount = Number(e[13]),
                t.totalVolume = Number(e[14]) || 0,
                t.exchange = e[15],
                t.futuresType = e[16],
                t.isHot = Number(e[18]),
                t.day5Highest = Number(e[19]),
                t.day5Lowest = Number(e[20]),
                t.day10Highest = Number(e[21]),
                t.day10Lowest = Number(e[22]),
                t.day20Highest = Number(e[23]),
                t.day20Lowest = Number(e[24]),
                t.day55Highest = Number(e[25]),
                t.day55Lowest = Number(e[26]),
                t.weighted = Number(e[27]),
                t.withNight = r[0] > "15:00",
                !0
            }
        }
        , E = new function() {
            var e, t = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gthkap());
                var a = t[10]
                  , r = t[11]
                  , n = (t[24],
                _({
                    dateStr: a,
                    dateDiv: "-",
                    timeStr: r,
                    hqObj: i,
                    tArr: e,
                    start: "16:30"
                }));
                i.date = n.datePart.date || new Date,
                i.isDateChange = n.datePart.isDateChange,
                i.today = n.datePart.today;
                var o = !1;
                (!i.time || n.timePart.time > "09:29" && i.time < n.timePart.time) && (o = !0),
                i.time = n.timePart.time,
                i.index = n.timePart.index,
                i.isUpdateTime = n.timePart.isUpdateTime,
                o && (i.isUpdateTime = !0),
                i.name = i.cnName || String(t[0]);
                var l = Number(t[2]) || Number(t[1]) || 0;
                return i.prevclose = l,
                i.open = Number(t[1]) || l,
                i.preopen = Number(t[2]) || Number(t[14]) || Number(t[24]) || l,
                i.price = Number(t[5]) || l,
                i.high = Number(t[3]) || l,
                i.low = Number(t[4]) || l,
                i.totalVolume = Number(t[9]) || 1e3 * Number(t[8]) || 0,
                i.totalAmount = Number(t[8]) || 0,
                !0
            }, i = function(e, t) {
                var i = e.split(",");
                !i || i.length < 15 || (t.type = String(i[0]).toLowerCase(),
                t.lastfive = 0,
                t.status = Number(i[14]),
                t.issueprice = Number(i[16]),
                t.cnName = i[19] || i[15],
                t.isAp = i[24] || "no")
            };
            this.update = function(e, a, r, n) {
                var s = !0;
                return r && i(r, a),
                e && (s = t(e, a, n)),
                s
            }
        }
        , R = new function() {
            var e, t = function(t, i, a) {
                if (!t)
                    return !1;
                e || (e = s.gthk());
                var r;
                a && (r = a.split(","),
                r[17] >= t[17] && (t[17] = r[17]),
                r[18] >= t[18] && (t[18] = r[18]));
                var n = t[17]
                  , o = t[18];
                window.HKisFake && (n === window.HkisFakeDateString.replace(/\-/g, "/") ? (window.HKisFake = !1,
                window.HKisFakeDateString = n) : (window.HKisFake = !0,
                o = "09:30",
                n = window.HkisFakeDateString.replace(/\-/g, "/")));
                var l = (t[24],
                _({
                    dateStr: n,
                    dateDiv: "/",
                    timeStr: o,
                    hqObj: i,
                    tArr: e,
                    start: "09:30"
                }));
                i.date = l.datePart.date || new Date,
                i.isDateChange = l.datePart.isDateChange,
                i.today = l.datePart.today;
                var u = !1;
                (!i.time || l.timePart.time > "09:29" && i.time < l.timePart.time) && (u = !0),
                i.time = l.timePart.time,
                i.index = l.timePart.index,
                i.isUpdateTime = l.timePart.isUpdateTime,
                l.timePart.isUpdateTime || i.time > "16:00" && i.time < "16:20" && (i.index = e.length - 1),
                u && (i.isUpdateTime = !0),
                i.name = i.cnName || String(t[1]);
                var m = Number(t[3]) || Number(t[2]) || 0;
                return i.prevclose = m,
                i.open = Number(t[2]) || m,
                i.preopen = Number(t[2]) || Number(t[9]) || Number(t[10]) || m,
                i.price = Number(t[6]) || m,
                i.high = Number(t[4]) || m,
                i.low = Number(t[5]) || m,
                i.totalVolume = Number(t[12]) || 1e3 * Number(t[11]) || 0,
                i.totalAmount = Number(t[11]) || 0,
                !0
            }, i = function(e, t) {
                var i = e.split(",");
                !i || i.length < 15 || (t.type = String(i[0]).toLowerCase(),
                t.lastfive = 0,
                t.status = Number(i[14]),
                t.issueprice = Number(i[16]),
                t.cnName = i[19] || i[15],
                t.isAp = i[24] || "no")
            };
            this.update = function(e, a, r, n) {
                var s = !0;
                return r && i(r, a),
                e && (s = t(e, a, n)),
                s
            }
        }
        , A = new function() {
            this.update = function(e, t) {
                if (!e)
                    return !1;
                var i = window["kke_global_index_" + t.symbol] && window["kke_global_index_" + t.symbol].time || [["06:00", "23:59"], ["00:00", "05:00"]]
                  , r = s.gata(a(t.symbol), i)
                  , n = r
                  , o = r[0]
                  , l = 6
                  , u = e[l]
                  , m = e[7];
                "znb_NKY" === t.symbol && "11:29" > m && m > "10:29" && (m = "10:29");
                var h = _({
                    dateStr: u,
                    timeStr: m,
                    tArr: n,
                    start: o,
                    hqObj: t
                });
                if (h.datePart.isErrData)
                    return !1;
                t.date = h.datePart.date,
                t.today = h.datePart.today,
                t.time = h.timePart.time,
                t.index = h.timePart.index,
                t.index < 0 && (t.time = d(i, t.time),
                t.index = r.indexOf(t.time)),
                t.isUpdateTime = h.timePart.isUpdateTime,
                t.name = String(e[0]);
                var c = Number(e[9]) || 0;
                return t.prevclose = c,
                t.open = Number(e[8]) || c,
                t.price = Number(e[1]) || c,
                t.high = Number(e[10]) || c,
                t.low = Number(e[11]) || c,
                t.buy = Number(e[9]),
                t.sell = Number(e[9]),
                t.totalVolume = Number(e[12]) || 0,
                t.holdingAmount = 0,
                !0
            }
        }
        , L = new function() {
            this.update = function(e, t) {
                if (!e)
                    return !1;
                var i = s.gtgds()
                  , a = i
                  , r = i[0]
                  , n = 12
                  , o = e[n]
                  , l = e[6]
                  , m = _({
                    dateStr: o,
                    timeStr: l,
                    tArr: a,
                    start: r,
                    hqObj: t
                });
                if (m.datePart.isErrData)
                    return !1;
                t.date = m.datePart.date,
                t.today = m.datePart.today,
                t.time = m.timePart.time,
                t.index = m.timePart.index,
                t.index < 0 && (t.time = d(u.GOODS, t.time),
                t.index = i.indexOf(t.time)),
                t.isUpdateTime = m.timePart.isUpdateTime,
                t.name = String(e[13]);
                var h = Number(e[7]) || 0;
                return t.prevclose = h,
                t.open = Number(e[8]) || h,
                t.price = Number(e[0]) || h,
                t.high = Number(e[4]) || h,
                t.low = Number(e[5]) || h,
                t.buy = Number(e[2]),
                t.sell = Number(e[3]),
                t.buyAmount = Number(e[10]),
                t.sellAmount = Number(e[11]),
                t.holdingAmount = Number(e[9]),
                t.withNight = !0,
                !0
            }
        }
        , F = new function() {
            this.update = function(e, t) {
                if (!e)
                    return !1;
                var i = window["kke_future_" + t.symbol] && window["kke_future_" + t.symbol].time || [["06:00", "23:59"], ["00:00", "05:00"]]
                  , r = s.gata(a(t.symbol), i)
                  , n = r
                  , o = r[0]
                  , l = 12
                  , u = e[l]
                  , m = e[6]
                  , h = _({
                    dateStr: u,
                    timeStr: m,
                    tArr: n,
                    start: o,
                    hqObj: t
                });
                if (h.datePart.isErrData)
                    return !1;
                t.date = h.datePart.date,
                t.today = h.datePart.today,
                t.time = h.timePart.time,
                t.index = h.timePart.index,
                t.index < 0 && (t.time = d(i, t.time),
                t.index = r.indexOf(t.time)),
                t.isUpdateTime = h.timePart.isUpdateTime,
                t.name = String(e[13]);
                var c = Number(e[7]) || Number(e[8]) || Number(e[0]) || 0;
                return t.prevclose = c,
                t.open = Number(e[8]) || c,
                t.price = Number(e[0]) || c,
                t.high = Number(e[4]) || c,
                t.low = Number(e[5]) || c,
                t.buy = Number(e[2]),
                t.sell = Number(e[3]),
                t.buyAmount = Number(e[10]),
                t.sellAmount = Number(e[11]),
                t.holdingAmount = Number(e[9]),
                !0
            }
        }
        , U = new function() {
            var e;
            this.update = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gta());
                var a = t[32]
                  , r = a.split(" ")
                  , n = r[0]
                  , o = r[1]
                  , l = _({
                    dateStr: n,
                    timeStr: o,
                    hqObj: i,
                    tArr: e,
                    start: "09:30"
                });
                if (l.datePart.isErrData)
                    return !1;
                i.date = l.datePart.date,
                i.isDateChange = l.datePart.isDateChange,
                i.today = l.datePart.today,
                i.time = l.timePart.time,
                i.index = l.timePart.index,
                i.index < 0 && (i.time = d(u.CN, i.time),
                i.index = e.indexOf(i.time)),
                i.isUpdateTime = l.timePart.isUpdateTime,
                i.name = String(t[37]),
                i.isNewListed = Boolean(0 == i.name.indexOf("N"));
                var m = Number(t[44]) || 0;
                return i.prevclose = m,
                i.preopen = Number(t[9]) || m,
                i.open = Number(t[9]) || m,
                i.price = Number(t[2]) || m,
                i.high = Number(t[39]) || m,
                i.low = Number(t[40]) || m,
                i.position = Number(t[5]) || 0,
                i.totalVolume = Number(t[41]) || 0,
                i.totalAmount = Number(t[42]) || 0,
                !0
            }
        }
        , H = new function() {
            var e;
            this.update = function(t, i) {
                if (!t)
                    return !1;
                e || (e = s.gta());
                var a = t[30]
                  , r = t[31]
                  , n = _({
                    dateStr: a,
                    timeStr: r,
                    hqObj: i,
                    tArr: e,
                    start: "09:30"
                });
                if (n.datePart.isErrData)
                    return !1;
                if (i.date = n.datePart.date,
                i.isDateChange = n.datePart.isDateChange,
                i.today = n.datePart.today,
                i.time = n.timePart.time,
                i.index = n.timePart.index,
                i.isUpdateTime = n.timePart.isUpdateTime,
                !n.timePart.isUpdateTime) {
                    var o = i.time.split(":")
                      , l = Number(o[0])
                      , m = Number(o[1]);
                    switch (l) {
                    case 11:
                        59 > m && (i.isUpdateTime = !0);
                        break;
                    case 15:
                        31 > m && (i.isUpdateTime = !0)
                    }
                }
                i.index < 0 && (i.time = d(u.CN, i.time),
                i.index = e.indexOf(i.time)),
                i.name = String(t[0]),
                i.isNewListed = Boolean(0 == i.name.indexOf("N"));
                var h = Number(t[2]) || 0;
                i.prevclose = h,
                i.preopen = Number(t[1]) || Number(t[6]) || Number(t[7]) || h,
                i.open = Number(t[1]) || h,
                i.price = Number(t[3]) || h,
                i.high = Number(t[4]) || h,
                i.low = Number(t[5]) || h,
                i.buy = Number(t[6]),
                i.sell = Number(t[7]),
                i.totalVolume = Number(t[8]) / 1e3 || 0,
                i.totalAmount = Number(t[9]) || 0;
                var c = t[32];
                return i.state = c,
                i.isStopDay = "02" == c || "03" == c,
                i.statusStr = p[c] || "",
                !0
            }
        }
        , B = [], j = "", X = "", Y = function(e) {
            for (var t = B.length; t--; )
                B[t](e),
                B[t] = null,
                B.length--
        };
        this.get = function(e, t) {
            var r, n = e.symbol, s = e.withI, o = n, l = 0;
            if (s)
                for (var u, m = n.split(","), d = m.length; d > l; l++) {
                    u = m[l];
                    var p;
                    p = "HK" == a(u) ? u.replace("rt_", "") + "_i" : u + "_i",
                    o += "," + p
                }
            var b, N;
            if (e.delay)
                j += n + ",",
                X += o + ",",
                B.push(t),
                clearTimeout(f),
                f = setTimeout(function() {
                    for (X = X.substring(0, X.length - 1),
                    j = j.substring(0, j.length - 1),
                    r = c(X),
                    N = r.length,
                    b = {
                        count: N
                    },
                    l = 0; N > l; l++)
                        v(r[l].join(","), i(h, null, j, Y, null, b), e);
                    j = "",
                    X = ""
                }, 100);
            else
                for (r = c(o),
                N = r.length,
                b = {
                    count: N
                },
                l = 0; N > l; l++)
                    v(r[l].join(","), i(h, null, n, t, null, b), e)
        }
        ,
        this.parse = function(t, i) {
            var a, n = t.symbol;
            switch (t.market) {
            case "CN_TR":
                a = r(n, null, t.hqStr);
                break;
            default:
                var s = S.kak(t.hqStr, t.market);
                a = h(n, null, s, null)
            }
            e.isFunc(i) && i(a)
        }
    };
    return h
});
;xh5_define("utils.painter", ["utils.util", "cfgs.settinger"], function(t, e) {
    "use strict";
    function i() {
        function e(t) {
            function e(t) {
                o = t.hd || o;
                var e = t.width || i.width || 0
                  , s = t.height || i.height || 0
                  , l = o;
                switch (i.style.width = e + "px",
                i.style.height = s + "px",
                l) {
                case 0:
                    break;
                case 1:
                    l = a.hdpr,
                    e *= l,
                    s *= l;
                    break;
                default:
                    e *= l,
                    s *= l
                }
                i.height = i.width = 0,
                i.height = s,
                i.width = e,
                l && 1 != l && n.scale(l, l)
            }
            this.VER = "2.0.1";
            var i = s("canvas");
            "undefined" != typeof FlashCanvas && FlashCanvas.initElement(i);
            var n = i.getContext("2d")
              , o = 1;
            t && e(t),
            this.canvas = i,
            this.g = n,
            this.resize = e
        }
        function i(i) {
            var s, a, o, l, r, c, f, d, _, m = i.parentObj, g = i.ctn, p = m.sd, v = m.setting, N = 0, T = v.DIMENSION.H_TIME_PART, S = m.nu, M = m.fixScale, k = 99999, b = function() {
                s = new e,
                a = s.canvas,
                o = s.g,
                a.style.position = "absolute",
                a.style.zIndex = 0,
                n.addHandler(a, "touchstart", function(t) {
                    v.custom.touch_prevent && n.preventDefault(t)
                }),
                g.appendChild(a)
            }, y = function(t) {
                t = t || {},
                l = v.DIMENSION.getStageW(),
                N = isNaN(t.mh) ? N : t.mh,
                r = v.DIMENSION.posX,
                c = v.DIMENSION.RIGHT_W,
                f = v.DIMENSION.K_RIGHT_W,
                d = isNaN(t.h) ? d : t.h,
                T = isNaN(t.eh) ? T : t.eh,
                s.resize({
                    width: l,
                    height: d + T + N,
                    hd: v.PARAM.getHd()
                }),
                o.font = v.STYLE.FONT_SIZE + "px " + v.STYLE.FONT_FAMILY
            }, O = function(t, e, i, s) {
                t = ~~(t + .5),
                t -= .5,
                e = ~~(e + .5),
                e -= .5,
                i = ~~(i + .5),
                i -= .5,
                o.beginPath(),
                s ? (o.moveTo(t, i),
                o.lineTo(e, i)) : (o.moveTo(i, t),
                o.lineTo(i, e)),
                o.stroke()
            }, K = function(t, e) {
                var i;
                return M ? i = isNaN(e) ? 0 > t ? Math.floor(t) : Math.ceil(t) : t.toFixed(e) : (t = (1e4 * t).toFixed(0),
                i = t / 1e4,
                i > k && (i = Math.floor(i))),
                i
            }, w = new function() {
                var e, i, s, a, n, u = 4, f = p.futureTime || window["kke_future_" + p.symbol], _ = function() {
                    if (!(p.business || !isNaN(v.custom.mini_threshold.height) && d < v.custom.mini_threshold.height)) {
                        var e = v.DIMENSION.extend_draw
                          , i = r;
                        e ? (o.textAlign = "left",
                        o.textBaseline = "top") : o.textAlign = "right",
                        o.fillStyle = v.COLOR.T_N,
                        o.strokeStyle = v.COLOR.GRID,
                        v.DIMENSION.getStageH() < 0 && "TFLOW" == p.name && (p.labelPriceCount = 4),
                        !p.isSC && v.DIMENSION.h_t < 150 && (p.labelPriceCount = 2);
                        for (var s, a, n, h, u, f = p.labelMaxP, _ = S ? t.strUtil.nu(f) : null, m = p.labelMinP, g = p.labelPriceCount, T = v.DIMENSION.posX, M = f - m, b = d / g, y = 0; g >= y; y++) {
                            u = y * b + N,
                            o.fillStyle = v.COLOR.T_N,
                            n = f - y * M / g,
                            n > 0 ? o.fillStyle = v.COLOR.T_RISE : 0 > n && (o.fillStyle = v.COLOR.T_FALL),
                            e ? y == g && (o.textBaseline = "bottom") : o.textBaseline = 0 == y ? "top" : y == g ? "bottom" : "middle";
                            var w;
                            if (p.isCompare) {
                                if (p.dAdd <= 1)
                                    n *= 100,
                                    h = n.toFixed(2),
                                    h += "%",
                                    o.fillText(h, T, u),
                                    o.fillText(h, T + v.DIMENSION.w_t + o.measureText(h).width, u);
                                else {
                                    w = p.datas[0][0].prevclose;
                                    var R, I = n;
                                    I *= 100,
                                    R = I.toFixed(2),
                                    R += "%",
                                    e ? o.fillText(R, v.DIMENSION.w_t - o.measureText(R).width, u) : o.fillText(R, T + v.DIMENSION.w_t + o.measureText(R).width, u),
                                    n = n * w + w,
                                    h = n.toFixed(2),
                                    o.fillText(h, T, u)
                                }
                                O(i, l - c, u, !0)
                            } else {
                                if (p.isSC)
                                    if (o.fillStyle = v.COLOR.K_P,
                                    S) {
                                        var D = p.name && "TFLOW" == p.name ? 2 : 0;
                                        n /= _[0],
                                        0 == y || y == g ? (h = y >= g ? _[1] : K(n, D),
                                        ("NaN" == h || "" == h) && (h = 0)) : h = ""
                                    } else
                                        h = 0 == y || y == g ? n.toFixed(1 > m ? 4 : 2) : 0,
                                        0 == h && 0 != y && y != g && (h = "");
                                else {
                                    if (v.DIMENSION.h_t < 0)
                                        return;
                                    w = p.datas[0][0].prevclose;
                                    var x = "HK" == p.market ? 3 : 4
                                      , L = 1 > m ? x : p.nfloat || 2;
                                    L = 0 > m ? 2 : p.nfloat || 2,
                                    "HF" == t.market(p.symbol) ? 3 > m ? L = 4 : 99 > m && (L = 3) : "HK" == p.market || "US" == p.market ? L = t.strUtil.nfloat(m) : "LSE" === p.market && (L = 3),
                                    p.ennfloat && (L = p.nfloat),
                                    h = Math.abs(n) > k ? Math.floor(n) : n.toFixed(L),
                                    s = 100 * (n - w) / Math.abs(w),
                                    o.fillStyle = s > 0 ? v.COLOR.T_RISE : 0 > s ? v.COLOR.T_FALL : v.COLOR.T_N,
                                    a = isNaN(s) ? "--%" : s.toFixed(2) + "%",
                                    isFinite(s) || (a = "--%"),
                                    e ? p.simple ? (0 === y || y === g) && o.fillText(a, T + v.DIMENSION.w_t - o.measureText(a).width, u) : o.fillText(a, T + v.DIMENSION.w_t - o.measureText(a).width, u) : o.fillText(a, T + v.DIMENSION.w_t + o.measureText(a).width, u)
                                }
                                p.simple ? (0 === y || y === g) && o.fillText(h, T, u) : (o.fillText(h, T, u),
                                O(i, l - c, u, !0))
                            }
                        }
                    }
                }, g = function(e) {
                    p && t.market(p.symbol),
                    v.DIMENSION.w_t;
                    p.simple || O(N, d + N, e, !1)
                }, T = function(t, i, s, a, n) {
                    if (!p.simple && (e = t,
                    m.dt)) {
                        var l = o.measureText(i).width
                          , r = 0;
                        if (r = 0 == s ? 0 : s == a - 1 ? -l : -l / 2,
                        0 == a && (r = n / 2 - l / 2),
                        p.business) {
                            o.font = "14px " + v.STYLE.FONT_FAMILY;
                            var h = 10;
                            (0 == s || s == a - 1) && o.fillText(i, t + r, N + d + v.STYLE.FONT_SIZE + 2 + h)
                        } else
                            o.fillText(i, t + r, N + d + v.STYLE.FONT_SIZE + 2)
                    }
                }, M = function(t) {
                    var e = t.replace("nf_", "").replace(/[\d]+$/, "");
                    return "TF" == e || "T" == e ? "CFF" : "NF"
                }, b = 30, w = "ignore", R = "ignoreT", I = function() {
                    var e, o = p && t.market(p.symbol);
                    switch (p && !p.isSC && "cb" == p.mt && (o = p.mt),
                    o) {
                    case "US":
                        u = 7;
                        break;
                    case "HK":
                        u = 5;
                        break;
                    case "NF":
                    case "HF":
                    case "globalbd":
                        u = 0;
                        break;
                    default:
                        u = 4
                    }
                    if (!i) {
                        switch (o) {
                        case "HF":
                            i = t.tUtil.gata(o, f && f.time || [["06:00", "23:59"], ["00:00", "05:00"]]);
                            break;
                        case "NF":
                            i = t.tUtil.gata(o, f && f.time || [["09:00", "23:29"], ["13:00", "02:59"]]);
                            break;
                        case "global_index":
                            i = t.tUtil.gata(o, f && f.time || [["06:00", "23:59"], ["00:00", "05:00"]]);
                            break;
                        case "cb":
                            var l = p.rangeTime;
                            i = t.tUtil.gata(o, l);
                            break;
                        default:
                            i = t.tUtil.gata(o)
                        }
                        for (("CFF" == M(p.symbol) || "hf_CHA50CFD" === p.symbol) && (b = 15),
                        s = [],
                        e = 0; e < i.length; e += b)
                            s.push(i[e]);
                        s[s.length - 1] !== i[i.length - 1] && (s[s.length - 1] = i[i.length - 1])
                    }
                    a = [],
                    n = [];
                    var r = v.DIMENSION.w_t
                      , h = 370
                      , c = 70
                      , d = 35
                      , _ = r / s.length
                      , g = 0
                      , N = 0;
                    if ("car" == v.custom.show_time_label && (c = 170),
                    m.dt && "HK" == o) {
                        var T = p.hq.time;
                        m.dt && T > "15:59" && (T > "16:09" && (T = "16:09"),
                        s[s.length - 1] = T),
                        h = 415
                    }
                    for (e = 0; e < s.length; e++)
                        0 == e || e == s.length - 1 ? (a.push(s[e]),
                        n.push(R)) : e == u ? (a.push(s[e]),
                        n.push(s[e])) : h > r ? a.push(w) : e > 0 && u > e ? _ * (e - g) > c && _ * (u - e) > c ? (a.push(s[e]),
                        g = e) : a.push(w) : (u > g && (g = u),
                        _ * (e - g) > c && _ * (s.length - 1 - e) > c ? (a.push(s[e]),
                        g = e) : a.push(w)),
                        0 != e && e != u && e != s.length - 1 && (e > 0 && u > e ? _ * (e - N) > d && _ * (u - e) > d ? (n.push(s[e]),
                        N = e) : n.push(R) : (u > N && (N = u),
                        _ * (e - N) > d && _ * (s.length - 1 - e) > d ? (n.push(s[e]),
                        N = e) : n.push(R)));
                    switch (o) {
                    case "NF":
                        f && ("21:00" != f.time[0][0] ? u = 15 == b ? v.DIMENSION._w <= 550 ? 9 : 0 : 4 : h > r && (u = Math.floor(n.length / 2))),
                        a[a.length - 1] = 30 == b ? "15:00" : "15:15";
                        var S = s[u].split(":");
                        59 == S[1] && (s[u] = Number(S[0]) + 1 + ":00"),
                        a[u] = s[u];
                        break;
                    case "HF":
                        h > r && (u = Math.floor(n.length / 2)),
                        a[u] = s[u];
                        break;
                    case "HKAP":
                        s = ["16:15", w, w, w, w, "18:30"],
                        a = ["16:15", w, w, w, w, "18:30"],
                        n = [R, R, R, "17:00", R, R]
                    }
                }, D = function() {
                    var i = v.DIMENSION.w_t;
                    if (isNaN(v.custom.mini_threshold.width) || !(i < v.custom.mini_threshold.width)) {
                        o.textBaseline = "bottom",
                        o.textAlign = "left",
                        o.strokeStyle = v.COLOR.TIME_L,
                        o.fillStyle = v.COLOR.TIME_S,
                        e = r;
                        var l = p.datas
                          , c = l.length
                          , f = p && t.market(p.symbol)
                          , d = s.length
                          , _ = 1;
                        "NF" == f && "CFF" == M(p.symbol) && (_ = 1);
                        var N = i / Math.max(d - _, 5)
                          , S = r
                          , k = 550;
                        if (v.DIMENSION.getStageH() < 0 && (m.dt = !0),
                        "car" == v.custom.show_time_label && (k = 850),
                        m.dt) {
                            var b;
                            if (1 == c || c > 6)
                                for (b = 0; d > b; b++)
                                    a[b] !== w && T(S, a[b], b, d),
                                    "HF" == f || "NF" == f ? a[b] !== w && n[b] !== R && (b == u ? g(S, u) : g(S)) : p.business || n[b] !== R && (b == u ? g(S, u) : g(S)),
                                    S += N;
                            else if (6 > c)
                                for (N = i / c,
                                b = 0; c > b; b++)
                                    v.DIMENSION._w < k ? T(S, h.ds(l[b][0].date, "/", !1, !0, !1, !1), b, 0, N) : T(S, h.ds(l[b][0].date, "/") + "/" + h.nw(l[b][0].date.getDay()), b, 0, N),
                                    0 != b && g(S),
                                    S += N
                        }
                    }
                };
                this.drawFrames = function() {
                    y(),
                    I(),
                    D(),
                    _()
                }
            }
            , R = new function() {
                this.iOffsetX = 0;
                var e, i, s, a, n, h = this, c = 0, g = 22, T = 99, M = function(t, e, i) {
                    if (isNaN(i)) {
                        if (c + T >= t || t >= l - T)
                            return;
                        O(N + 1, d + N, t, !1)
                    }
                    if (c = t,
                    m.dt) {
                        var s, a = d + N + v.STYLE.FONT_SIZE + 3;
                        switch (i) {
                        case 1:
                            o.fillText(e, t, a);
                            break;
                        case 2:
                            s = o.measureText(e).width,
                            o.fillText(e, t - s, a);
                            break;
                        case 3:
                            break;
                        default:
                            s = o.measureText(e).width,
                            o.fillText(e, t - (s >> 1), a)
                        }
                    }
                }, k = function() {
                    var e = v.DIMENSION.w_k;
                    if (isNaN(v.custom.mini_threshold.width) || !(e < v.custom.mini_threshold.width)) {
                        o.textBaseline = "bottom",
                        o.textAlign = "left",
                        o.strokeStyle = v.COLOR.TIME_L,
                        o.fillStyle = v.COLOR.TIME_S,
                        c = r;
                        var i, s = p.datas, a = s.length;
                        switch (_) {
                        case u.URLHASH.KMS:
                            i = "sec";
                            break;
                        case u.URLHASH.K1:
                            i = "h";
                            break;
                        case u.URLHASH.K5:
                        case u.URLHASH.K15:
                        case u.URLHASH.K30:
                        case u.URLHASH.K60:
                        case u.URLHASH.K240:
                            i = 60 / _ * 24 > a ? "h" : "d";
                            break;
                        case u.URLHASH.KD:
                        case u.URLHASH.KDF:
                        case u.URLHASH.KDB:
                        case u.URLHASH.KCL:
                        case u.URLHASH.KCLF:
                        case u.URLHASH.KCLB:
                            i = a > 300 ? "y" : 28 > a ? "w" : "m";
                            break;
                        default:
                            i = a > 300 ? "y" : "m"
                        }
                        for (var n, l, f, d, m, N, S = e / Math.max(a, v.PARAM.minCandleNum), k = h.iOffsetX + r + .6 * S, b = e / T, y = e / (S * g), O = Math.ceil(y / b), K = 0, w = 0, R = -1, I = -1, D = -1, x = -1, L = -1, C = 0; a > C; C++)
                            if (N = s[C],
                            m = N.date,
                            l = m.getMonth(),
                            n = m.getFullYear(),
                            0 != C)
                                if (C >= a - 1)
                                    M(k + S / 2, n + "/" + (l + 1) + "/" + m.getDate(), a >= v.PARAM.minCandleNum ? 2 : 3);
                                else {
                                    if ("car" != v.custom.show_time_label)
                                        switch (i) {
                                        case "sec":
                                            var E = m.getSeconds();
                                            E != x && (E = t.strUtil.zp(E),
                                            d = t.strUtil.zp(m.getMinutes()),
                                            f = t.strUtil.zp(m.getHours()),
                                            M(k, f + ":" + d + ":" + E)),
                                            x = Number(E);
                                            break;
                                        case "min":
                                            d = m.getMinutes(),
                                            d != D && (d = t.strUtil.zp(d),
                                            f = t.strUtil.zp(m.getHours()),
                                            M(k, f + ":" + d)),
                                            D = Number(d);
                                            break;
                                        case "h":
                                            f = m.getHours(),
                                            f != I && (d = t.strUtil.zp(m.getMinutes()),
                                            M(k, f + ":" + d)),
                                            I = f;
                                            break;
                                        case "d":
                                            var F = m.getDate();
                                            F != K && M(k, n + "/" + (l + 1) + "/" + F),
                                            K = F;
                                            break;
                                        case "w":
                                            var H = m.getDay();
                                            L > H && M(k, l + 1 + "/" + m.getDate()),
                                            L = H;
                                            break;
                                        default:
                                        case "m":
                                            l == R || l % O || M(k, n + "/" + (l + 1)),
                                            R = l;
                                            break;
                                        case "y":
                                            n != w && M(k, n),
                                            w = n
                                        }
                                    k += S
                                }
                            else
                                M(r, n + "/" + (l + 1) + "/" + m.getDate(), 1)
                    }
                }, b = 37, w = function() {
                    o.fillStyle = v.COLOR.K_PCT,
                    o.textBaseline = "top",
                    o.textAlign = "right";
                    for (var t, e, i = p.nfloat || 2, s = p.prevclose, a = p.labelPriceCount, n = 0, r = d / a, h = p.labelMaxP, c = p.labelMinP, m = h - c; a >= n; n++)
                        if (!(b > r && 1 & n)) {
                            e = n * r + N,
                            0 == n && e++,
                            t = h - n * m / a,
                            n == a && (o.textBaseline = "bottom");
                            var g;
                            _ === u.URLHASH.KMS || _ === u.URLHASH.K1 ? (g = ((t - s) / s * 100).toFixed(i) + "%",
                            o.fillStyle = t > s ? v.COLOR.K_MS_RISE : s > t ? v.COLOR.K_MS_FALL : v.COLOR.K_MS_N) : g = Math.round((t - s) / s * 100) + "%",
                            o.fillText(g, l - f, e)
                        }
                }, R = function() {
                    if (p && p.hq) {
                        var e;
                        switch (v.custom.k_0pct) {
                        case "hq":
                            e = p.hq.prevclose;
                            break;
                        case "range":
                            e = p.prevclose;
                            break;
                        default:
                            return
                        }
                        var i = t.xh5_PosUtil.pp(e, p.labelMinP, p.labelMaxP, d) + N;
                        i = ~~(i + .5),
                        i -= .5;
                        var s = r
                          , a = 5;
                        for (o.beginPath(); l - f > s; )
                            o.moveTo(s, i),
                            s += a,
                            o.lineTo(s, i),
                            s += a;
                        o.strokeStyle = v.COLOR.T_PREV,
                        o.stroke()
                    }
                }, I = function() {
                    if (isNaN(v.custom.mini_threshold.height) || !(d < v.custom.mini_threshold.height)) {
                        var e = v.DIMENSION.extend_draw;
                        o.fillStyle = v.COLOR.K_P,
                        o.strokeStyle = v.COLOR.GRID;
                        var i = r;
                        e ? (o.textAlign = "left",
                        o.textBaseline = "top") : o.textAlign = "right";
                        for (var s, a, n, h = p.labelPriceCount, c = 0, m = v.DIMENSION.posX, g = d / h, T = p.labelMaxP, M = p.labelMinP, k = T - M, y = p.prevclose, I = S ? t.strUtil.nu(T) : null; h >= c; c++)
                            b > g && 1 & c || (a = c * g + N,
                            0 == c && a++,
                            s = T - c * k / h,
                            p.isCompare && (s *= 100),
                            S ? (s /= I[0],
                            n = c >= h ? I[1] : K(s)) : n = K(s),
                            p.isCompare && (n += "%"),
                            e ? c == h && (o.textBaseline = "bottom") : o.textBaseline = 0 == c ? "top" : c == h ? "bottom" : "middle",
                            _ === u.URLHASH.KMS && y && (o.fillStyle = s > y ? v.COLOR.K_MS_RISE : y > s ? v.COLOR.K_MS_FALL : v.COLOR.K_MS_N),
                            o.fillText(n, m, a),
                            O(i, l - f, a, !0));
                        y && (p.isCompare || (v.custom.show_k_rangepercent && w(),
                        "no" != v.custom.k_0pct && R()))
                    }
                };
                this.drawFrames = function(t) {
                    (t || p.datas[0].date != s || p.datas[p.datas.length - 1].date != a || p.labelMaxP != e || p.labelMinP != i || _ != n) && (y(),
                    I(),
                    k()),
                    n = p.viewState.viewId,
                    s = p.datas[0].date,
                    a = p.datas[p.datas.length - 1].date,
                    e = p.labelMaxP,
                    i = p.labelMinP
                }
            }
            ;
            this.drawBg = function(t, e) {
                p.datas && (_ = p.viewState.viewId,
                v.datas.isT ? w.drawFrames(t) : (isNaN(e) || (R.iOffsetX = e,
                t = !0),
                R.drawFrames(t)))
            }
            ,
            this.respos = function(t) {
                y(t),
                a.style.left = 0,
                a.style.top = v.DIMENSION.posY + "px",
                this.drawBg(!0)
            }
            ,
            this.gc = function() {
                t.domGc(a)
            }
            ,
            b()
        }
        function f(e) {
            var i, a = e.parentObj, h = e.ctn, c = a.iMgr, u = r(a.iTo, null, h), f = a.iClk, d = c.globalDragHandler, _ = c.zoomView, m = c.shortClickHandler, g = a.setting, p = g.PARAM.isFlash, v = !p, N = !1, T = 300, S = {
                isM: !1,
                isTch: !1,
                isP: !1,
                tCount: void 0,
                tXOff: -1,
                isPv: !1,
                lastIy: null,
                mDx: 0 / 0,
                mDy: 0 / 0,
                isClk: 0,
                isTMin: !1,
                mvOx: 0,
                vP: function(t) {
                    var e, i;
                    if (t.changedTouches) {
                        n.preventDefault(t),
                        n.stopPropagation(t);
                        var s = n.getTarget(t)
                          , a = t.changedTouches[0]
                          , o = s.getBoundingClientRect()
                          , l = o.left
                          , r = o.top;
                        e = a.clientX - l,
                        i = a.clientY - r
                    } else
                        e = t.offsetX,
                        isNaN(e) && (e = t.layerX),
                        i = t.offsetY,
                        isNaN(i) && (i = t.layerY);
                    u(e, i, t)
                },
                vH: function(t) {
                    if (!(this.isClk > 0) && g.custom.allow_move) {
                        n.preventDefault(t),
                        n.stopPropagation(t);
                        var e = t.changedTouches ? t.changedTouches[0].pageX : t.layerX;
                        isNaN(e) && (e = t.offsetX);
                        var i = t.changedTouches ? t.changedTouches[0].pageY : t.layerY;
                        isNaN(i) && (i = t.offsetY),
                        d(this.mDx, e, this.mDy, i)
                    }
                },
                mD: function(t) {
                    this.mDx = isNaN(t.layerX) ? t.offsetX : t.layerX,
                    this.mDy = isNaN(t.layerY) ? t.offsetY : t.layerY,
                    this.isM = this.isP = !0,
                    this.isClk = 2,
                    b(!0)
                },
                mM: function(t) {
                    this.isTch || (N = !0,
                    this.isClk--,
                    this.isP ? this.vH(t) : this.vP(t))
                },
                mU: function(t) {
                    this.mDx = 0 / 0,
                    this.mDy = 0 / 0,
                    this.isM = this.isP = !1,
                    d(0 / 0, 0 / 0, 0 / 0, 0 / 0, t),
                    this.isClk > 0 && f && (this.isClk = 0,
                    f()),
                    b(!1)
                },
                mO: function() {
                    this.isClk = 0,
                    this.isM = this.isP = N = !1,
                    u(0 / 0, 0 / 0),
                    b(!1)
                },
                tR: function() {
                    clearTimeout(this.tCount),
                    this.isPv = this.isTMin = !1
                },
                gR: function() {
                    this.tR(),
                    this.tXOff = -1
                },
                tCheck: function(t) {
                    this.mvOx = t.touches[0].pageX;
                    var e = this;
                    e.isClk = 2,
                    this.tCount = setTimeout(function() {
                        e.isPv = !0,
                        e.vP(t),
                        e.isClk = 0
                    }, T)
                },
                tE: function(t) {
                    g.custom.touch_prevent && n.preventDefault(t),
                    this.isPv || m(),
                    this.tR(),
                    this.isTch = N = !1,
                    this.mDx = 0 / 0,
                    this.mDy = 0 / 0,
                    u(0 / 0, 0 / 0),
                    d(0 / 0, 0 / 0, 0 / 0, 0 / 0, t),
                    this.isClk > 0 && f && (this.isClk = 0,
                    f())
                },
                tM: function(t) {
                    if (this.isClk--,
                    1 == t.touches.length) {
                        if (!this.isPv && !this.isTMin && Math.abs(this.mvOx - t.touches[0].pageX) < 5)
                            return;
                        this.isTMin = !0,
                        clearTimeout(this.tCount),
                        this.isPv ? this.vP(t) : this.vH(t)
                    } else if (2 == t.touches.length) {
                        n.preventDefault(t),
                        n.stopPropagation(t);
                        var e = t.touches[0]
                          , i = t.touches[1];
                        if (this.tXOff >= 0) {
                            var s = Math.abs(e.pageX - i.pageX);
                            if (s != this.tXOff) {
                                var a = n.getTarget(t)
                                  , o = l.pageX(a)
                                  , r = e.pageX - o
                                  , h = i.pageX - o;
                                _(s < this.tXOff, [r, h])
                            }
                        }
                        this.tXOff = Math.abs(e.pageX - i.pageX)
                    }
                },
                tS: function(t) {
                    switch (this.tR(),
                    g.custom.touch_prevent && n.preventDefault(t),
                    this.isTch = N = !0,
                    this.lastIy = t.touches[0].pageY,
                    this.mDx = t.changedTouches[0].pageX,
                    this.mDy = t.changedTouches[0].pageY,
                    t.touches.length) {
                    case 1:
                        this.tCheck(t);
                        break;
                    case 2:
                        this.gR()
                    }
                },
                handleEvent: function(t) {
                    if (g.custom.mouse_and_touch)
                        switch (t.type) {
                        case "mouseup":
                            this.mU(t);
                            break;
                        case "mousedown":
                            this.mD(t);
                            break;
                        case "mouseout":
                            this.mO();
                            break;
                        case "mousemove":
                            this.mM(t);
                            break;
                        case "touchend":
                            this.tE(t);
                            break;
                        case "touchmove":
                            this.tM(t);
                            break;
                        case "touchstart":
                            this.tS(t)
                        }
                }
            }, M = new function() {
                this.onmouseup = function(t) {
                    g.custom.mouse_and_touch && S.mU(t)
                }
                ,
                this.onmousedown = function(t) {
                    g.custom.mouse_and_touch && S.mD(t)
                }
                ,
                this.onmouseout = function() {
                    g.custom.mouse_and_touch && S.mO()
                }
                ,
                this.onmousemove = function(t) {
                    g.custom.mouse_and_touch && S.mM(t)
                }
            }
            , k = function() {
                v ? i = s("canvas") : (i = s("div"),
                i.style.backgroundColor = "#eee",
                i.style.opacity = 0,
                i.style.filter = "alpha(opacity=0)"),
                i.style.position = "absolute",
                i.style.zIndex = g.PARAM.I_Z_INDEX;
                var t;
                o.istd ? t = ["touchend", "touchmove", "touchstart"] : (t = ["mousedown", "mouseup", "mousemove", "mouseout"],
                o.allowt && (t = t.concat(["touchend", "touchmove", "touchstart"])));
                for (var e = t.length; e--; )
                    v ? n.addHandler(i, t[e], S) : n.addHandler(i, t[e], M["on" + t[e]] || function() {}
                    );
                h.appendChild(i)
            }, b = function(t) {
                t ? (i.style.cursor = "grabbing",
                i.style.cursor = "-webkit-grabbing") : i.style.cursor = "default"
            };
            this.respos = function(t) {
                i.style.top = g.DIMENSION.posY + t.mh + "px",
                i.style.left = g.DIMENSION.posX + "px";
                var e;
                e = g.datas.isT ? g.DIMENSION.w_t : g.DIMENSION.w_k,
                i.style.width = e + "px",
                i.style.height = t.h + "px"
            }
            ,
            this.gc = function() {
                t.domGc(i)
            }
            ,
            k()
        }
        function d(e) {
            this.VER = "2.3.0",
            e = c({
                setting: void 0,
                sd: void 0,
                ctn: void 0,
                reO: void 0,
                withHBg: !1,
                nu: !1,
                dt: !0,
                fixScale: !0,
                iTo: function() {},
                iMgr: void 0,
                iClk: void 0
            }, e || {});
            var n, o, l, r, h, u = e.setting, d = function() {
                e.ctn ? n = e.ctn : (n = s("div"),
                n.style.position = "relative")
            }, _ = function() {
                o = s("canvas"),
                "undefined" != typeof FlashCanvas && FlashCanvas.initElement(o),
                o.style.position = "absolute",
                o.style.zIndex = u.PARAM.G_Z_INDEX,
                l = o.getContext("2d"),
                n.appendChild(o)
            }, m = function() {
                h = new f({
                    parentObj: e,
                    ctn: n
                })
            }, g = function() {
                r = new i({
                    parentObj: e,
                    ctn: n
                })
            }, p = function(t) {
                t = t || {};
                var e, i, s = isNaN(t.mh) ? u.DIMENSION.H_T_T : t.mh, l = isNaN(t.eh) ? u.DIMENSION.H_TIME_PART : t.eh, c = u.PARAM.getHd();
                switch (e = u.datas.isT ? u.DIMENSION.w_t : u.DIMENSION.w_k,
                i = isNaN(t.h) ? u.DIMENSION.h_k : t.h,
                t.h = i,
                t.mh = s,
                t.eh = l,
                n.style.height = i + s + l + "px",
                o.style.top = u.DIMENSION.posY + s + "px",
                o.style.left = u.DIMENSION.posX + "px",
                o.style.width = e + "px",
                o.style.height = i + "px",
                c) {
                case 0:
                    break;
                case 1:
                    c = a.hdpr,
                    e *= c,
                    i *= c;
                    break;
                default:
                    e *= c,
                    i *= c
                }
                o.width = e,
                o.height = i,
                h && h.respos(t),
                r && r.respos(t)
            };
            this.resize = p,
            this.getCanvas = function() {
                return o
            }
            ,
            this.getG = function() {
                return l
            }
            ,
            this.getWrap = function() {
                return n
            }
            ;
            var v;
            this.scale = function(t) {
                switch (t) {
                case 0:
                    return;
                case 1:
                    t = a.hdpr
                }
                t && l.scale(t, t)
            }
            ,
            this.newGStyle = function(t) {
                for (var e in t)
                    t.hasOwnProperty(e) && (l[e] = t[e])
            }
            ,
            this.newStyle = function(t, e, i) {
                v = l.strokeStyle = t,
                e && l.beginPath(),
                i && (l.lineWidth = i)
            }
            ,
            this.newFillStyle = function(t, e) {
                if (t && !(t.length < 1)) {
                    var i = t.length;
                    if (1 == i)
                        l.fillStyle = t[0];
                    else if (i > 1) {
                        for (var s = l.createLinearGradient(0, 0, 0, e), a = 0; i > a; a++)
                            s.addColorStop(1 / (i - 1) * a, t[a]);
                        l.fillStyle = s
                    }
                }
            }
            ,
            this.newFillStyle_rgba = function(e, i, s) {
                for (var a = t.isArr(s) ? s : [s], n = l.createLinearGradient(0, 0, 0, i), o = 0, r = e.length; r > o; o++)
                    n.addColorStop(1 / (r - 1) * o, t.hex2dec(e[o], a[o] || 0));
                l.fillStyle = n
            }
            ,
            this.clear = function(t, e) {
                o.width = o.width,
                t && (v && l.strokeStyle != v && (l.strokeStyle = v),
                l.beginPath()),
                this.scale(e)
            }
            ,
            this.clearLimit = function(t, e) {
                l.clearRect(t, 0, e, o.height),
                l.beginPath()
            }
            ,
            this.beginPath = function() {
                l.beginPath()
            }
            ,
            this.closePath = function() {
                l.closePath()
            }
            ,
            this.fill = function() {
                l.fill()
            }
            ,
            this.stroke = function() {
                l.stroke()
            }
            ,
            this.save = function() {
                l.save()
            }
            ,
            this.translate = function(t, e) {
                l.translate(t, e)
            }
            ,
            this.restore = function() {
                l.restore()
            }
            ,
            this.drawTxt = function(t, e, i, s, a) {
                if (l.fillStyle = s.color,
                l.textBaseline = s.base || "top",
                l.textAlign = s.align || "left",
                void 0 != a) {
                    var n = l.measureText(t).width;
                    e + n > a && (e = a - n)
                }
                l.fillText(t, e, i)
            }
            ,
            this.moveTo = function(t, e) {
                l.moveTo(t, e)
            }
            ,
            this.lineTo = function(t, e) {
                l.lineTo(t, e)
            }
            ,
            this.drawDot = function(t, e, i, s) {
                s && l.moveTo(t, e),
                l.arc(t, e, i, 0, 2 * Math.PI)
            }
            ,
            this.arc = function(t, e, i, s, a, n) {
                l.arc(t, e, i, s, a, n)
            }
            ,
            this.drawCandleRect = function(t, e, i, s, a, n) {
                if (e != i && !(2 > s)) {
                    var o = i - e;
                    t += .5 * s,
                    s = ~~(s + .5),
                    t = ~~(t + .5),
                    e = ~~(e + .5),
                    o = ~~(o + .5),
                    l.lineWidth = 1,
                    n ? (t -= .5,
                    e -= .5,
                    l.strokeStyle = a,
                    l.strokeRect(t, e, s, o)) : (1 > o && (o = 1),
                    l.fillStyle = a,
                    l.fillRect(t, e, s, o),
                    t -= .5,
                    e -= .5,
                    l.strokeStyle = a,
                    l.strokeRect(t, e, s, o))
                }
            }
            ,
            this.drawCandleRect_solid = function(t, e, i, s, a) {
                if (e != i && !(2 > s)) {
                    var n = i - e;
                    t += .5 * s,
                    s = ~~(s + .5),
                    t = ~~(t + .5),
                    e = ~~(e + .5),
                    n = ~~(n + .5),
                    l.lineWidth = 1,
                    l.fillStyle = a,
                    l.fillRect(t, e, s, n),
                    t -= .5,
                    e -= .5,
                    l.strokeStyle = a,
                    l.strokeRect(t, e, s, n)
                }
            }
            ,
            this.drawCandleLineRect = function(t, e, i, s, a, n, o, r) {
                if (t += n,
                t = ~~(t + .5),
                l.strokeStyle = o,
                l.lineWidth = 1,
                e != a) {
                    if (t -= .5,
                    l.moveTo(t, e),
                    r && n >= 2) {
                        var h = Math.min(i, s)
                          , c = Math.max(i, s);
                        l.lineTo(t, h),
                        l.moveTo(t, c)
                    }
                    l.lineTo(t, a)
                }
                if (i == s) {
                    var u = .5 * n;
                    u = ~~(u + .5),
                    .5 > u && (u = .5),
                    i = ~~(i + .5),
                    i -= .5,
                    l.moveTo(t - u, i),
                    l.lineTo(t + u, i)
                }
            }
            ,
            this.drawOhlc = function(t, e, i, s, a, n, o) {
                l.strokeStyle = o,
                l.lineWidth = 1;
                var r = .5 * n;
                r = ~~(r + .5),
                .5 > r && (r = .5),
                t += n,
                t = ~~(t + .5),
                e = ~~(e + .5),
                e -= .5,
                l.moveTo(t - r, e),
                l.lineTo(t, e),
                a = ~~(a + .5),
                a -= .5,
                l.moveTo(t, a),
                l.lineTo(t + r, a),
                t -= .5,
                l.moveTo(t, i),
                l.lineTo(t, s)
            }
            ,
            this.drawVStickC = function(t, e, i, s, a) {
                t += i,
                i = ~~(i + .5),
                1 > i && (i = 1),
                t = ~~(t + .5),
                1 & i && (t -= .5),
                e = ~~(e + .5),
                s = ~~(s - .5),
                l.strokeStyle = a,
                l.lineWidth = i,
                l.moveTo(t, e),
                l.lineTo(t, e + s)
            }
            ,
            this.drawVStickRect = function(t, e, i, s, a, n) {
                var o = i;
                t = ~~(t + .5),
                o > 11 && (t += 1),
                o = ~~(o + .5),
                e = ~~(e + .5),
                s = ~~(s + .5),
                0 == s && (s = 1),
                n ? (.5 > o && (o = .5),
                l.fillStyle = a,
                l.fillRect(t, e, o, s)) : (t -= .5,
                e -= .5,
                l.strokeStyle = a,
                l.strokeRect(t, e, o, s))
            }
            ,
            this.drawRect = function(t, e, i, s, a) {
                if (e != i) {
                    var n = i - e;
                    s = ~~(s + .5),
                    t = ~~(t + .5),
                    e = ~~(e + .5),
                    n = ~~(n + .5),
                    l.lineWidth = 1,
                    l.fillStyle = a,
                    l.fillRect(t, e, s, n)
                }
            }
            ,
            this.drawBg = function(t) {
                r && r.drawBg(!1, t)
            }
            ,
            this.remove = function() {
                t.domGc(o),
                h && h.gc(),
                r && r.gc()
            }
            ,
            d(),
            _(),
            e.withHBg && (m(),
            g()),
            p(e.reO)
        }
        this.xh5_ibPainter = d,
        this.xh5_Canvas = e
    }
    var s = t.$C
      , a = t.xh5_BrowserUtil
      , n = t.xh5_EvtUtil
      , o = t.xh5_deviceUtil
      , l = t.xh5_HtmlPosUtil
      , r = t.fBind
      , h = t.dateUtil
      , c = t.oc
      , u = e.globalCfg;
    return i
});
;