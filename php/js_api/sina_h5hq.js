xh5_define("datas.k", ["utils.util"], function(e) {
    "use strict";
    var t = e.load
      , a = e.dateUtil
      , n = e.kUtil
      , s = e.xh5_S_KLC_D
      , r = 0 == location.protocol.indexOf("https:");
    return new function() {
        this.VER = "2.8.0";
        var o = {
            globalbd: {
                DAYK_URL: "http://quotes.sina.cn/bd/api/jsonp.php/$cb/GlobalBondYieldService.getDayLine?refresh=1&symbol=$symbol"
            },
            CNKCB: {
                DAYK_URL: "http://quotes.sina.cn/cn/api/jsonp.php/$cb/KC_MarketDataService.getKLineData?symbol=$symbol"
            },
            CN: {
                MINK_URL: "http://quotes.sina.cn/cn/api/jsonp_v2.php/$cb/CN_MarketDataService.getKLineData?symbol=$symbol&scale=$scale&ma=no&datalen=1023",
                DAYK_URL_PHP: "//quotes.sina.cn/hq/api/openapi.php/MarketCenterService.getDailyK?market=cn&symbol=$symbol&start=2019-01-01&asc=1&callback=$cb",
                DAYK_URL_OLD: "http://finance.sina.com.cn/realstock/company/$symbol/hisdata/klc_kl.js?d=$rn",
                DAYK_URL: "http://finance.sina.com.cn/realstock/company/$symbol/hisdata_klc2/klc_kl.js?d=$rn",
                DAYK_RE_URL: "http://finance.sina.com.cn/realstock/company/$symbol/$dirfq.js",
                RE_VAR: "$symbol$dirfq"
            },
            HK: {
                MINK_URL: "",
                DAYK_URL: "http://finance.sina.com.cn/stock/hkstock/$symbol/klc_kl.js?d=$rn",
                DAYK_RE_URL: "http://finance.sina.com.cn/stock/hkstock/$symbol/$dirfq.js",
                RE_VAR: "$symbol$dirfq"
            },
            US: {
                MINK_URL: "http://stock.finance.sina.com.cn/usstock/api/jsonp_v2.php/$cb/US_MinKService.getMinK?symbol=$symbol&type=$scale&___qn=3",
                DAYK_URL: "http://finance.sina.com.cn/staticdata/us/$symbol",
                DAYK_RE_URL: "https://finance.sina.com.cn/us_stock/company/reinstatement/$symbol_$dirfq.js",
                RE_VAR: "$symbol_$dirfq"
            },
            option_cn: {
                DAYK_URL: "http://stock.finance.sina.com.cn/futures/api/jsonp_v2.php/$cb/StockOptionDaylineService.getSymbolInfo?symbol=$symbol"
            },
            op_m: {
                DAYK_URL: "http://stock.finance.sina.com.cn/futures/api/jsonp.php/$cb/FutureOptionAllService.getOptionDayline?symbol=$symbol"
            },
            forex: {
                DAYK_URL: "http://vip.stock.finance.sina.com.cn/forex/api/jsonp.php/$cb/NewForexService.getDayKLine?symbol=$symbol&_=$rn",
                MINK_URL: "http://vip.stock.finance.sina.com.cn/forex/api/jsonp.php/$cb/NewForexService.getMinKline?symbol=$symbol&scale=$scale&datalen=$datalen"
            },
            forex_yt: {
                DAYK_URL: "http://vip.stock.finance.sina.com.cn/forex/api/jsonp.php/$cb/NewForexService.getDayKLine?symbol=$symbol&_=$rn",
                MINK_URL: "http://vip.stock.finance.sina.com.cn/forex/api/jsonp.php/$cb/NewForexService.getOldMinKline?symbol=$symbol&scale=$scale&datalen=$datalen"
            },
            OTC: {
                DAYK_URL: "http://stock.finance.sina.com.cn/thirdmarket/api/jsonp.php/$cb/ThirdDataService.ThirdDailyData?symbol=$symbol&_=$rn"
            },
            CFF: {
                DAYK_URL: "http://stock2.finance.sina.com.cn/futures/api/jsonp.php/$cb/CffexFuturesService.getCffexFuturesDailyKLine?symbol=$symbol&_=$rn",
                MINK_URL: "http://stock2.finance.sina.com.cn/futures/api/jsonp.php/$cb/CffexFuturesService.getCffexFuturesMiniKLine$scalem?symbol=$symbol&_=$rn"
            },
            HF: {
                DAYK_URL: "http://stock2.finance.sina.com.cn/futures/api/jsonp.php/$cb/GlobalFuturesService.getGlobalFuturesDailyKLine?symbol=$symbol&_=$rn&source=web",
                INIT_URL: "http://stock.finance.sina.com.cn/futures/api/jsonp.php/$cb/InterfaceInfoService.getMarket?category=hf&symbol=$symbol",
                MINK_URL: "http://gu.sina.cn/ft/api/jsonp.php/$cb/GlobalService.getMink?symbol=$symbol&type=$scale",
                INIT_VAR_PRE: "kke_future_"
            },
            NF: {
                DAYK_URL: "http://stock2.finance.sina.com.cn/futures/api/jsonp.php/$cb/InnerFuturesNewService.getDailyKLine?symbol=$symbol&_=$rn",
                MINK_URL: "http://stock2.finance.sina.com.cn/futures/api/jsonp.php/$cb/InnerFuturesNewService.getFewMinLine?symbol=$symbol&type=$scale",
                INIT_URL: "http://stock.finance.sina.com.cn/futures/api/jsonp.php/$cb/InterfaceInfoService.getMarket?category=nf&symbol=$symbol",
                INIT_VAR_PRE: "kke_future_"
            },
            global_index: {
                DAYK_URL: "http://stock.finance.sina.com.cn/usstock/api/jsonp.php/$cb/Global_IndexService.getDayLine?symbol=$symbol&num=100",
                INIT_URL: "http://stock.finance.sina.com.cn/usstock/api/jsonp.php/$cb/Global_IndexService.getTradeTime?symbol=$symbol&category=index",
                INIT_VAR_PRE: "kke_global_index_"
            },
            GOODS: {
                DAYK_URL: "http://stock2.finance.sina.com.cn/futures/api/jsonp.php/$cb/SpotService.getDaily?symbol=$symbol"
            },
            BTC: {
                DAYK_URL: "http://quotes.sina.cn/fx/api/openapi.php/BtcService.getDayKLine?symbol=$symbol&callback=$cb",
                MINK_URL: "http://quotes.sina.cn/fx/api/openapi.php/BtcService.getMinKline?symbol=$symbol&scale=$scale&datalen=$datalen&callback=$cb"
            },
            LSE: {
                DAYK_URL: "http://quotes.sina.cn/lse/api/jsonp.php/$cb/LSEService.getDays?symbol=$symbol"
            },
            MSCI: {
                DAYK_URL: "http://finance.sina.com.cn/staticdata/msci/$symbol"
            }
        };
        o.REPO = o.CN;
        var l = function() {
            return {
                msg: "",
                data: null
            }
        }
          , i = function(t, s, r) {
            var o = S(r)
              , l = r.symbol
              , i = r.newthour
              , c = 1
              , u = o.market;
            "CN" == u && (c = s && /[gz]/.test(s.type) ? 10 : e.isRepos(l) ? 10 : 100),
            e.isRepos(l) && (c = 10),
            e.isCNK(l) && (c = 100),
            t || (t = []);
            var m = 0 / 0
              , p = "";
            if (s && s.date) {
                var b, h = s.date, d = !1;
                if (t.length > 0 ? (b = t[t.length - 1],
                h || (h = b.date)) : d = !0,
                b)
                    if ("NF" === u || "GOODS" === u)
                        a.stbd(b.date, h) ? 1 != s.iscff && s.withNight && s.time >= i ? d = !0 : s.open && s.price && (b.open = s.open,
                        b.high = s.high,
                        b.low = s.low,
                        b.close = s.price,
                        b.volume = s.totalVolume * c) : h < b.date || (d = !0);
                    else if (a.stbd(b.date, h))
                        "hf_CHA50CFD" === s.symbol && s.time >= i ? d = !0 : s.date && s.open && s.price && (b.open = s.open,
                        b.high = s.high,
                        b.low = s.low,
                        b.close = s.price,
                        b.volume = s.totalVolume * c,
                        b.date = a.ddt(h),
                        b.postAmt = s.postAmount,
                        b.postVol = s.postVolume * c);
                    else if (h < b.date)
                        ;
                    else if (i)
                        if ("hf_CHA50CFD" === s.symbol)
                            d = !0;
                        else if (s.time >= i)
                            d = !0;
                        else {
                            var f = (h - b.date) / 1e3 / 24 / 60 / 60;
                            d = f >= 2
                        }
                    else
                        d = !0;
                if (d) {
                    var y = s.totalVolume * c;
                    t.push({
                        open: s.open,
                        high: s.high,
                        low: s.low,
                        close: s.price,
                        volume: y,
                        date: a.ddt(h),
                        postAmt: s.postAmount,
                        postVol: s.postVolume
                    })
                }
                m = s.issueprice,
                p = s.name
            }
            if (t.length < 1)
                return [t, void 0, void 0, void 0];
            var _ = !isNaN(m) && m > 0 ? m : t[0].open;
            e.oc(t[0], {
                prevclose: _,
                name: p,
                symbol: l
            });
            var v = n.mw(t, s, _, c, o.endDay)
              , g = v[0]
              , k = v[1]
              , N = v[2]
              , $ = void 0;
            if (n.pd(t, null),
            n.pd(g, null),
            n.pd(k, null),
            n.pd(N, null),
            s && s.settlement) {
                var w = t[t.length - 1];
                w.ampP = w.amplitude / s.settlement,
                w.change = w.close - s.settlement,
                w.percent = w.change / s.settlement
            }
            return e.oc(g[0], {
                name: p,
                symbol: l
            }),
            e.oc(k[0], {
                name: p,
                symbol: l
            }),
            e.oc(N[0], {
                name: p,
                symbol: l
            }),
            r.ytd && ($ = n.yd(t),
            e.oc($[0], {
                name: p,
                symbol: l
            })),
            [t, g, k, $, N]
        }
          , c = function(t, a, n) {
            var s = e.market(t);
            "SI" == s && (s = "CN");
            var l = s ? o[s][a ? "MINK_URL" : "DAYK_URL"] : null;
            return /^GN|gn|HY|hy|DY|dy\d{7}$/.test(t) && "CN" == s && (l = o[s][a ? "MINK_URL" : "DAYK_URL_OLD"]),
            (r || n) && (l = e.getSUrl(l)),
            l
        }
          , u = function(t, a) {
            var n, s, l = e.market(t);
            return o[l] && (n = o[l].DAYK_RE_URL,
            s = o[l].RE_VAR),
            n && (r || a) && (n = e.getSUrl(n)),
            {
                url: n,
                VAR: s,
                market: l
            }
        }
          , m = function(t, a) {
            var n, s, l, i = e.market(t);
            return o[i] && (n = o[i].INIT_URL,
            s = o[i].INIT_VAR,
            l = o[i].INIT_VAR_PRE),
            n && (r || a) && (n = e.getSUrl(n)),
            {
                url: n,
                VAR: s,
                varPre: l,
                market: i
            }
        }
          , p = {
            xh5Fund: function(e) {
                for (var t, a, n, s, r = new Date, o = [r.getFullYear(), r.getMonth() + 1, r.getDate()].join("_"), l = e.data, i = e.symbol, c = l.split("#"), u = [], m = [], p = [], b = [], h = [], d = [], f = c.length; f--; )
                    s = c[f].split(","),
                    t = s[0].slice(0, 4),
                    a = s[0].slice(4, 6),
                    n = s[0].slice(6, 8),
                    n = [t, a, n].join("-"),
                    u.push({
                        d: n,
                        c: s[1]
                    }),
                    m.push({
                        d: n,
                        c: s[2]
                    }),
                    p.push({
                        d: n,
                        c: s[3]
                    }),
                    b.push({
                        d: n,
                        c: s[4]
                    }),
                    h.push({
                        d: n,
                        c: s[5]
                    }),
                    d.push({
                        d: n,
                        c: s[6]
                    });
                var y = ["_dwjz_", i, o].join("")
                  , _ = ["_ljjz_", i, o].join("")
                  , v = ["_lshb_", i, o].join("")
                  , g = ["_pwbfbyd_", i, o].join("")
                  , k = ["_pwbfbjd_", i, o].join("")
                  , N = ["_pwbfbnd_", i, o].join("")
                  , $ = ["_fh_", i, o].join("");
                window[y] = u,
                window[_] = m,
                window[v] = p,
                window[g] = b,
                window[k] = h,
                window[N] = d,
                window[$] = {
                    fhday: e.fhday,
                    fhvalue: e.fhvalue,
                    fhchaifen: e.fhchaifen
                }
            }
        }
          , b = function(e) {
            var t = [];
            if (e)
                for (var a, n, s = 0, r = e.length; r > s; s++) {
                    n = e[s],
                    a = Number(n.c);
                    var o = n.d.split("-");
                    t.push({
                        close: a,
                        open: Number(n.o) || a,
                        high: Number(n.h) || a,
                        low: Number(n.l) || a,
                        volume: Number(n.v) || 0,
                        date: new Date(Number(o[0]),Number(o[1]) - 1,Number(o[2]),0),
                        postVol: Number(n.pv) || 0,
                        postAmt: Number(n.pa) || 0
                    })
                }
            return t
        }
          , h = function(e) {
            var t = [];
            if (e)
                for (var a, n, s = e.split("|"), r = 0, o = s.length; o > r; r++)
                    a = s[r].split(","),
                    a.length < 5 || (n = a[0].split("-"),
                    t.push({
                        open: Number(a[1]),
                        low: Number(a[2]),
                        high: Number(a[3]),
                        close: Number(a[4]),
                        volume: Number(a[5]),
                        date: new Date(Number(n[0]),Number(n[1]) - 1,Number(n[2]),0)
                    }));
            return t
        }
          , d = function(e) {
            var t = [];
            if (e && e.result && e.result.data)
                for (var a, n, s = e.result.data, r = s.split("|"), o = 0, l = r.length; l > o; o++)
                    a = r[o].split(","),
                    a.length < 5 || (n = a[0].split("-"),
                    t.push({
                        open: Number(a[1]),
                        low: Number(a[2]),
                        high: Number(a[3]),
                        close: Number(a[4]),
                        volume: Number(a[5]),
                        date: new Date(Number(n[0]),Number(n[1]) - 1,Number(n[2]),0)
                    }));
            return t
        }
          , f = function(e) {
            var t = [];
            if (e && e.length)
                for (var a, n, s = .001, r = e.split("|"), o = 0, l = 0, i = r.length; i > l; l++)
                    a = r[l].split(","),
                    a.length < 5 || (n = a[0].split("-"),
                    o = Number(a[4]) || o,
                    t.push({
                        open: Number(a[1]) || o,
                        low: Number(a[2]) || o,
                        high: Number(a[3]) || o,
                        close: Number(a[4]) || o,
                        volume: Number(a[5]) * s,
                        date: new Date(Number(n[0]),Number(n[1]) - 1,Number(n[2]),0)
                    }));
            return t
        }
          , y = function(e) {
            var t = [];
            if (e)
                for (var a, n, s, r = 0, o = e.length; o > r; r++)
                    a = e[r],
                    n = a[0].split("-"),
                    s = Number(a[4]),
                    t.push({
                        date: new Date(Number(n[0]),Number(n[1]) - 1,Number(n[2]),0),
                        open: Number(a[1]) || s,
                        high: Number(a[2]) || s,
                        low: Number(a[3]) || s,
                        close: s,
                        volume: Number(a[5]) || 0
                    });
            return t
        }
          , _ = function(e) {
            var t = [];
            if (e)
                for (var a, n, s = e.length; s--; )
                    a = e[s],
                    n = Number(a[4]),
                    t.push({
                        day: a[0],
                        open: Number(a[1]) || n,
                        high: Number(a[2]) || n,
                        low: Number(a[3]) || n,
                        close: n,
                        volume: Number(a[5]) || 0
                    });
            return t
        }
          , v = function(e) {
            var t = [];
            if (e)
                for (var n, s, r = 0, o = e.length; o > r; r++)
                    n = e[r],
                    s = Number(n.close),
                    t.push({
                        date: a.sd(n.date),
                        volume: Number(n.volume),
                        open: Number(n.open) || s,
                        high: Number(n.high) || s,
                        low: Number(n.low) || s,
                        close: s
                    });
            return t
        }
          , g = function(e, t) {
            if (!e)
                return null;
            for (var a, n = t.vu || 1, s = 0, r = e.length; r > s; s++)
                a = e[s],
                a.high *= 1,
                a.open *= 1,
                a.low *= 1,
                a.close *= 1,
                a.volume *= n;
            return e
        }
          , k = function(e) {
            if (!e)
                return null;
            for (var t, n = 0, s = e.length; s > n; n++)
                t = e[n],
                t.high = 1 * t.h,
                t.open = 1 * t.o,
                t.low = 1 * t.l,
                t.close = 1 * t.c,
                t.volume = 1 * t.v,
                t.day = t.d,
                t.date = a.sd(t.d);
            return e
        }
          , N = function(e) {
            if (!e)
                return null;
            for (var t, n = 0, s = e.length; s > n; n++)
                t = e[n],
                t.high = 1 * t.h,
                t.open = 1 * t.o,
                t.low = 1 * t.l,
                t.close = 1 * t.c,
                t.volume = 1 * t.v,
                t.date = a.sd(t.d);
            return e
        }
          , $ = function(t, n, s, r) {
            for (var o, l, i = e.market(r.hqSb), c = "BTC" == i ? 0 : ("DINIW" == r.hqSb,
            6), u = n.length; u-- && 0 != u; )
                for (var m = n[u], p = n[u - 1], b = a.ssd(m.day), h = a.ssd(p.day), d = u; h.setMinutes(h.getMinutes() + s) < b; ) {
                    if (o = h.getDay(),
                    6 == o) {
                        if (l = h.getHours(),
                        l >= c)
                            continue
                    } else {
                        if (0 == o)
                            continue;
                        if (1 == o && (l = h.getHours(),
                        c > l))
                            continue
                    }
                    var f = e.clone(p, null);
                    f.day = a.dss(h),
                    n.splice(d++, 0, f)
                }
            for (var y = n[n.length - 1], _ = a.ssd(y.day); _.setMinutes(_.getMinutes() + s) < t; ) {
                if (o = _.getDay(),
                6 == o) {
                    if (l = _.getHours(),
                    l >= c)
                        continue
                } else {
                    if (0 == o)
                        continue;
                    if (1 == o && (l = _.getHours(),
                    c > l))
                        continue
                }
                var v = {
                    open: y.close,
                    high: y.close,
                    low: y.close,
                    close: y.close,
                    day: a.dss(_),
                    prevclose: y.prevclose
                };
                "BTC" == i && (v.volume = 0),
                n.push(v),
                y = v,
                _ = a.ssd(y.day)
            }
        }
          , w = function(t, n, s) {
            var r = e.market(s.hqSb)
              , o = "BTC" == r ? 0 : ("DINIW" == s.hqSb,
            6)
              , l = n[n.length - 1].day
              , i = l.split(" ")[0];
            if (a.stbds(t.date, i, null)) {
                var c, u, m, p = t.prevclose, b = t.date.getHours();
                if (o > b) {
                    var h, d = !1;
                    for (c = n.length; c-- && (h = !1,
                    m = n[c],
                    u = Number(m.day.split(" ")[1].split(":")[0]),
                    !d && o > u ? h = !0 : u >= o && (d = !0,
                    h = !0),
                    h); )
                        m.prevclose = p
                } else
                    for (c = n.length; c-- && (m = n[c],
                    u = Number(m.day.split(" ")[1].split(":")[0]),
                    u >= o); )
                        m.prevclose = p
            }
        }
          , D = function(t, n) {
            if (!t)
                return null;
            var s, r, o = Number(n.scale), l = e.market(n.hqSb);
            n.hqObjs && (s = n.hqObjs[n.hqSb],
            r = new Date(1e3 * n.hqObjs[n.withsymbol].hqstr)),
            r || (r = new Date);
            var i = 60 * r.getTimezoneOffset() * 1e3;
            r.setTime(r.getTime() + i),
            r.setHours(r.getHours() + 8);
            for (var c, u, m = 0, p = t.length; p > m; m++)
                if (u = t[m],
                u.high = 1 * u.h,
                u.open = 1 * u.o,
                u.low = 1 * u.l,
                u.close = 1 * u.c,
                "BTC" == l && (u.volume = 1 * u.v),
                o > 1) {
                    var b = a.ssd(u.d);
                    b.setMinutes(b.getMinutes() + o),
                    u.day = a.dss(b)
                } else
                    u.day = u.d,
                    isNaN(u.p) || (c = u.p),
                    isNaN(c) && (c = u.o),
                    u.prevclose = 1 * c;
            return $(r, t, o, n),
            1 == o && s && w(s, t, n),
            t
        }
          , R = function(e, t) {
            return e && e.result && e.result.data ? (e = e.result.data,
            D(e, t)) : null
        }
          , S = function(t) {
            var a, n = t.symbol, s = t.volunit || 1, r = e.market(n), o = !1;
            t.dataurl && t.dataurl.length > 1 ? a = t.dataurl : (/^(CN|HK|US|REPO|MSCI|SI)/.test(r) && (o = !0),
            a = c(n, !!t.ismink, t.ssl));
            var l, i, u, m = n, p = n;
            switch (r) {
            case "globalbd":
                p = m.replace("globalbd_", "");
                break;
            case "HK":
                m = 0 == n.indexOf("rt_") ? n : "rt_" + n,
                p = m.substring(5);
                break;
            case "US":
                m = 0 == n.indexOf("gb_") ? n : "gb_" + n,
                p = m.split("_")[1],
                p = p.replace("$", "."),
                p = p.toUpperCase(),
                l = k;
                break;
            case "op_m":
                p = m.replace("P_OP_", "");
                break;
            case "SI":
            case "CN":
            case "REPO":
                s = .01,
                e.isCNK(m) && (s = .01);
                break;
            case "forex":
            case "forex_yt":
                l = D,
                i = h,
                u = 5;
                break;
            case "BTC":
                p = m.replace("btc_", ""),
                l = R,
                i = d,
                u = 5;
                break;
            case "OTC":
                p = n.replace("sb", "otc_"),
                i = f;
                break;
            case "CFF":
                var g = m.split("_");
                p = g[g.length - 1],
                i = y,
                l = _;
                break;
            case "HF":
                m = 0 == n.indexOf("hf_") ? n : "hf_" + n,
                p = m.split("_")[1],
                i = v,
                l = k;
                break;
            case "NF":
                m = 0 == n.indexOf("nf_") ? n : "nf_" + n,
                p = m.split("_")[1],
                i = b,
                l = k;
                break;
            case "global_index":
                m = 0 == n.indexOf("znb_") ? n : "znb_" + n,
                p = m.split("_")[1],
                i = N;
                break;
            case "LSE":
                m = 0 == n.indexOf("lse_") ? n : "lse_" + n,
                p = m.split("_")[1],
                m = e.strUtil.replaceStr(m),
                i = N;
                break;
            case "MSCI":
                m = 0 == n.indexOf("msci_") ? n : "msci_" + n,
                p = n.replace("msci_", ""),
                i = b;
                break;
            case "GOODS":
                m = 0 == n.indexOf("gds_") ? n : "gds_" + n,
                p = m.split("_")[1],
                i = N
            }
            return t.customksb && (p = t.customksb),
            {
                hqSb: m,
                kSb: p,
                dayDataHandler: i,
                minDataHandler: l,
                endDay: u,
                kUrl: a,
                isCompressData: o,
                vu: s,
                market: r
            }
        }
          , K = function(a, s) {
            var r = S(a)
              , o = new Date
              , i = [o.getFullYear(), o.getMonth() + 1, o.getDate()].join("_")
              , c = a.scale
              , u = a.$scale || "$scale"
              , m = a.datalen || 828
              , p = "_" + r.kSb.replace(/\W/g, "") + "_" + c + "_" + o.getTime()
              , b = function(o) {
                var b = o ? o.dataObj : void 0
                  , h = l();
                t(r.kUrl.replace("$symbol", r.kSb).replace(u, c).replace("$cb", "var%20" + p + "=").replace("$rn", i).replace("$datalen", m), function() {
                    var t = window[p]
                      , o = a.dataformatter || r.minDataHandler || g;
                    if (t = o(t, {
                        vu: r.vu,
                        withsymbol: a.withsymbol,
                        hqSb: r.hqSb,
                        hqObjs: b,
                        scale: c
                    })) {
                        var l = {};
                        1 == c && (/^forex/.test(r.market) || /^BTC/.test(r.market)) && (l.usePc = !0),
                        n.pd(t, l),
                        h.data = t
                    } else
                        h.msg = "error";
                    e.isFunc(s) && s(h)
                }, function() {
                    h.msg = "error",
                    e.isFunc(s) && s(h)
                }, {
                    market: r.market,
                    symbol: r.hqSb,
                    type: "mink"
                })
            };
            a.withsymbol ? KKE.api("datas.hq.get", {
                symbol: [a.withsymbol, r.hqSb].join(","),
                cancelEtag: !0,
                ssl: a.ssl
            }, b) : b()
        };
        window.RELOAD_DK_DATA = 1;
        var L = function(a, n) {
            var r = S(a)
              , c = function(c) {
                var u = c ? c.data[0] : void 0
                  , m = l()
                  , p = new Date
                  , h = [p.getFullYear(), p.getMonth() + 1, p.getDate()].join("_")
                  , d = "_" + r.kSb.replace(/\W/g, "") + h
                  , f = "MSCI" === r.market || "US" === r.market || "CN" == r.market || "REPO" == r.market || "SI" == r.market ? "K2_" : "KL_";
                /^GN|gn|HY|hy|DY|dy\d{7}$/.test(r.hqSb) && "CN" == r.market && (f = "KL_");
                var y = /baiduboxapp/.test(navigator.userAgent.toLowerCase());
                y && "sh000001" == r.hqSb && (r.isCompressData = !1,
                r.kUrl = o.CN.DAYK_URL_PHP);
                var _ = function(e) {
                    var t = [];
                    if (e && e.result && e.result.data)
                        for (var a, n, s = e.result.data, r = 0, o = s.length; o > r; r++)
                            a = s[r],
                            n = s[r].day.split("-"),
                            t.push({
                                open: Number(a.open),
                                low: Number(a.low),
                                high: Number(a.high),
                                close: Number(a.close),
                                volume: Number(a.volume),
                                date: new Date(Number(n[0]),Number(n[1]) - 1,Number(n[2]),0)
                            });
                    return t
                };
                t(r.kUrl.replace("$symbol", r.kSb).replace("$rn", h).replace("$cb", "var%20" + d + "="), function() {
                    var t;
                    if (r.isCompressData) {
                        var o = r.kSb.replace(".", "$");
                        t = window["KLC_" + f + o],
                        t = s(t)
                    } else {
                        t = window[d];
                        var l = a.dataformatter || r.dayDataHandler || b;
                        y && "CN" == r.market && (l = _),
                        t = l(t)
                    }
                    var c = i(t, u, a);
                    c ? m.data = {
                        hq: u,
                        day: c[0],
                        week: c[1],
                        month: c[2],
                        ytd: c[3] || null,
                        year: c[4]
                    } : m.msg = "error",
                    e.isFunc(n) && n(m)
                }, function() {
                    if (u) {
                        var t = i(null, u, a);
                        t ? m.data = {
                            hq: u,
                            day: t[0],
                            week: t[1],
                            month: t[2],
                            ytd: t[3] || null,
                            year: t[4]
                        } : m.msg = "error",
                        e.isFunc(n) && n(m)
                    } else
                        m.msg = "error",
                        m.data = {
                            hq: u
                        },
                        e.isFunc(n) && n(m)
                }, {
                    market: r.market,
                    symbol: r.hqSb,
                    type: "k"
                })
            };
            "undefined" == typeof r.market || "UNKNOWN" === r.market ? c() : KKE.api("datas.hq.get", {
                symbol: r.hqSb,
                cancelEtag: !0,
                withI: !0,
                ssl: a.ssl
            }, c)
        }
          , U = function(t, a) {
            var s = t.staticdata
              , r = l();
            if (t.ismink)
                n.pd(s, null),
                r.data = s;
            else {
                var o = i(s, null, t);
                r.data = {
                    day: o[0],
                    week: o[1],
                    month: o[2],
                    ytd: o[3] || null,
                    year: o[4]
                }
            }
            e.isFunc(a) && a(r)
        };
        this.get = function(t, a) {
            t.staticdata ? U(t, a) : (t.wfn && e.isFunc(p[t.wfn]) && (window[t.wfn] = p[t.wfn]),
            t.ismink ? K(t, a) : L(t, a))
        }
        ,
        this.loadReData = function(a, n) {
            var s = l()
              , r = {
                HK: a.symbol.replace("rt_hk", ""),
                US: a.symbol.replace("gb_", "").replace("$", ".").toUpperCase(),
                CN: a.symbol
            }[a.market.toUpperCase()]
              , o = u(a.symbol, a.ssl)
              , i = o.url;
            if (!i)
                return s.msg = "error",
                void (e.isFunc(n) && n(s));
            var c = a.dir
              , m = o.VAR || "";
            m = m.replace("$symbol", r).replace("$dir", c).replace(".", "$"),
            "HK" === a.market && (m = "hk" + m);
            var p = new Date
              , b = p.getHours();
            t(i.replace("$symbol", r).replace("$dir", c).replace("$rn", b), function() {
                var t = window[m];
                window[m] = null,
                t && t.total > 0 ? s.data = t.data : s.msg = "error",
                e.isFunc(n) && n(s)
            }, function() {
                s.msg = "error",
                e.isFunc(n) && n(s)
            }, {
                market: o.market,
                symbol: r,
                type: "rek"
            })
        }
        ,
        this.loadHFInit = function(a, n) {
            var s = l()
              , r = a.symbol
              , o = m(r, a.ssl)
              , i = o.url
              , c = o.varPre
              , u = c + r
              , p = window[u];
            p ? (s.data = p,
            e.isFunc(n) && n(s)) : (r = r.split("hf_")[1],
            t(i.replace("$cb", "var%20" + u + "=").replace("$symbol", r), function() {
                p = window[u],
                p ? s.data = p : (window[u] = null,
                s.msg = "error, illegal data"),
                e.isFunc(n) && n(s)
            }, function() {
                s.msg = "error",
                e.isFunc(n) && n(s)
            }, {
                market: o.market,
                symbol: r,
                type: "init_hf"
            }))
        }
        ,
        this.loadNFInit = function(a, n) {
            var s = l()
              , r = a.symbol
              , o = m(r, a.ssl)
              , i = o.url
              , c = o.varPre
              , u = c + r
              , p = window[u];
            p ? (s.data = p,
            e.isFunc(n) && n(s)) : (r = r.match(/^nf_([a-zA-Z]+)\d+$/)[1],
            t(i.replace("$cb", "var%20" + u + "=").replace("$symbol", r), function() {
                p = window[u],
                p ? s.data = p : (window[u] = null,
                s.msg = "error, illegal data"),
                e.isFunc(n) && n(s)
            }, function() {
                s.msg = "error",
                e.isFunc(n) && n(s)
            }, {
                market: o.market,
                symbol: r,
                type: "init_nf"
            }))
        }
        ,
        this.loadGBInit = function(a, n) {
            var s = l()
              , r = a.symbol
              , o = m(r, a.ssl)
              , i = o.url
              , c = o.varPre
              , u = c + r
              , p = window[u];
            p ? (s.data = p,
            e.isFunc(n) && n(s)) : (r = r.split("znb_")[1],
            t(i.replace("$cb", "var%20" + u + "=").replace("$symbol", r), function() {
                p = window[u],
                p ? s.data = p : (window[u] = null,
                s.msg = "error, illegal data"),
                e.isFunc(n) && n(s)
            }, function() {
                s.msg = "error",
                e.isFunc(n) && n(s)
            }, {
                market: o.market,
                symbol: r,
                type: "init_global"
            }))
        }
    }
});
;xh5_define("chart.h5k", ["cfgs.settinger", "utils.util", "utils.painter"], function(e, t, n) {
    "use strict";
    function a(a) {
        function i(e, n) {
            function i(e) {
                O.setDataRange(e),
                y && (y.linkData(e),
                y.setDataRange()),
                N && (N.linkData(e),
                N.setDataRange()),
                w && (w.linkData(e),
                w.setDataRange())
            }
            function l(e, t) {
                var n, a, i = x.get(_.URLHASH.KD), o = i.length;
                e || (n = 0),
                t || (a = o - 1);
                for (var s = 0; o > s && (isNaN(n) && i[s].date >= e && (n = s),
                isNaN(a) && i[s].date >= t && (a = s),
                isNaN(n) || isNaN(a)); s++)
                    ;
                return [n, a]
            }
            function c() {
                n && (K = x),
                F.uUpdate(null, !0),
                "CN" !== u || /^(sh0|sh1|sh5|sz1|sz399)\d+/i.test(e.symbol) || x.initExtraData()
            }
            e = p({
                symbol: void 0,
                datas: {
                    day: {
                        wfn: void 0,
                        url: void 0,
                        dataformatter: void 0,
                        staticdata: void 0
                    },
                    min: {
                        wfn: void 0,
                        url: void 0,
                        dataformatter: void 0,
                        staticdata: void 0
                    }
                }
            }, e || {});
            var h = this
              , u = t.market(e.symbol)
              , g = !0;
            this.isErr = !1,
            this.symbol = e.symbol,
            this.market = u;
            var b;
            switch (u) {
            case "forex":
            case "forex_yt":
                "DINIW" == this.symbol,
                b = "06:00";
                break;
            case "BTC":
                b = "00:00";
                break;
            case "LSE":
                b = "08:00";
                break;
            default:
                b = "09:30"
            }
            this.isMain = n,
            this.isCompare = !1,
            this.datas = null,
            this.dataLen = 0,
            this.nfloat = e.nfloat || 2,
            this.dataLenOffset = 0,
            this.prevclose = 0 / 0,
            this.labelMaxP = 0,
            this.labelMinP = Number.MAX_VALUE,
            this.maxPrice = 0,
            this.minPrice = Number.MAX_VALUE,
            this.rangeMax = 0,
            this.rangeMin = Number.MAX_VALUE,
            this.labelMaxVol = 0,
            this.maxVolume = 0,
            this.minPercent = Number.MAX_VALUE,
            this.maxPercent = -Number.MAX_VALUE,
            this.labelPriceCount = 0 / 0,
            this.isTotalRedraw = !0,
            this.hq = void 0,
            this.nco = void 0;
            var y, N, w, S = new k(this,e), I = e.name;
            this.getName = function() {
                return I || ""
            }
            ,
            this.viewState = V;
            var x = new function() {
                var i, o = {}, s = {
                    rsAmount: void 0
                }, r = function(e, a, s, r, l) {
                    if (a) {
                        if (n) {
                            if (e == _.URLHASH.KD && (i = t.clone(a, null)),
                            r && window.datelist && h.hq) {
                                var c = t.xh5_S_KLC_D(window.datelist);
                                a = t.kUtil.ayd(a, c, !1, a[0].date, h.hq.date)
                            }
                        } else
                            l || (e == _.URLHASH.KD && (i = t.clone(a, null)),
                            a = t.kUtil.adbd(a, K.get(e), s, !1));
                        o["k" + e] = a;
                        var d = a.length
                          , u = r ? L.PARAM.K_CL_NUM : L.PARAM.defaultCandleNum;
                        o["k" + e + "v"] = d > u ? d - u : 0,
                        o["k" + e + "b"] = d
                    }
                }, l = function() {
                    var e = V.viewId;
                    switch (e) {
                    case _.URLHASH.KDF:
                    case _.URLHASH.KDB:
                        e = _.URLHASH.KD;
                        break;
                    case _.URLHASH.KWF:
                    case _.URLHASH.KWB:
                        e = _.URLHASH.KW;
                        break;
                    case _.URLHASH.KMF:
                    case _.URLHASH.KMB:
                        e = _.URLHASH.KM;
                        break;
                    case _.URLHASH.KYF:
                    case _.URLHASH.KYB:
                        e = _.URLHASH.KY;
                        break;
                    case _.URLHASH.KCLF:
                    case _.URLHASH.KCLB:
                        e = _.URLHASH.KCL
                    }
                    return e
                };
                this.get = function(e) {
                    if (t.isStr(e)) {
                        var n = l();
                        return o["k" + n + e]
                    }
                    return o["k" + (e || V.viewId)]
                }
                ,
                this.set = function(e, t) {
                    var n = l()
                      , a = "k" + n + e;
                    "undefined" != typeof o[a] && (o[a] = t)
                }
                ,
                this.getOriDK = function() {
                    return i
                }
                ,
                this.initState = r,
                this.initDWMState = function(e, n) {
                    var a = t.clone(n.day, null);
                    r(_.URLHASH.KD, n.day),
                    r(_.URLHASH.KW, n.week),
                    r(_.URLHASH.KM, n.month),
                    r(_.URLHASH.KCL, a, !1, !0),
                    r(_.URLHASH.KY, n.year)
                }
                ,
                this.extraDataObj = s,
                this.initExtraData = function() {
                    var n = "http://stock.finance.sina.com.cn/stock/api/jsonp.php/$cb/StockService.getAmountBySymbol?_=$rn&symbol=$symbol";
                    a.ssl && (n = t.getSUrl(n));
                    var i = "KKE_ShareAmount_" + e.symbol;
                    t.load(n.replace("$symbol", e.symbol).replace("$rn", String((new Date).getDate())).replace("$cb", "var%20" + i + "="), function() {
                        var e = window[i];
                        if (e) {
                            for (var t, n = [], a = e.length; a--; )
                                t = e[a],
                                n.push({
                                    amount: Number(t.amount),
                                    date: m.sd(t.date)
                                });
                            n.length && (s.rsAmount = n)
                        }
                    })
                }
                ,
                this.gc = function() {
                    o = null,
                    s = null
                }
            }
              , O = new function() {
                var e = function() {
                    h.minPrice = Number.MAX_VALUE,
                    h.maxPrice = -Number.MAX_VALUE,
                    h.minPercent = Number.MAX_VALUE,
                    h.maxPercent = -Number.MAX_VALUE,
                    h.maxVolume = 0,
                    h.rangeMax = 0,
                    h.rangeMin = Number.MAX_VALUE
                }
                  , t = function() {
                    for (var e, t = 0, n = h.dataLen; n > t; t++)
                        e = h.datas[t],
                        e.close <= 0 || (e.high > h.maxPrice && (h.maxPrice = h.rangeMax = e.high),
                        e.low < h.minPrice && (h.minPrice = h.rangeMin = e.low),
                        h.maxVolume = Math.max(h.maxVolume, e.volume));
                    var a = v(h.maxVolume, 0, 0, !0);
                    h.labelMaxVol = a[0],
                    h.maxPercent = Math.max((h.maxPrice - h.prevclose) / h.prevclose, 0),
                    h.minPercent = Math.min((h.minPrice - h.prevclose) / h.prevclose, 0)
                };
                this.createPlayingData = function() {
                    var e, t, n = L.DIMENSION.h_k, a = n * L.DIMENSION.P_HV, i = n * (1 - L.DIMENSION.P_HV);
                    e = h.labelMinP,
                    t = h.labelMaxP;
                    for (var o, s = h.labelMaxVol, r = h.prevclose, l = h.isTotalRedraw ? 0 : h.dataLen - h.dataLenOffset, c = L.custom.show_underlay_vol, u = h.isCompare ? "ppp" : "pp", p = h.dataLen; p > l; l++)
                        o = h.datas[l],
                        o.cy = d[u](o.close, e, t, n, r),
                        o.oy = d[u](o.open, e, t, n, r),
                        o.hy = d[u](o.high, e, t, n, r),
                        o.ly = d[u](o.low, e, t, n, r),
                        c && (o.vy = d.vp(o.volume, s, a) + i)
                }
                ,
                this.setDataRange = function(n) {
                    var i = x.get();
                    if (i) {
                        V.dataLength = i.length;
                        var o = V.start
                          , s = V.end;
                        if (isNaN(o) || isNaN(s))
                            s = x.get("b"),
                            o = x.get("v"),
                            V.start = o,
                            V.end = s;
                        else {
                            if (n && s + 1 >= i.length) {
                                var r = i.length - s;
                                V.end = s = i.length,
                                (1 == a.pcm || V.viewId == _.URLHASH.K1) && (0 == o && s > 1 && s < L.PARAM.minCandleNum && (o = s - 1,
                                V.start = o),
                                s - o >= L.PARAM.defaultCandleNum && (o += r,
                                V.start = o))
                            }
                            x.set("v", o),
                            x.set("b", s)
                        }
                        switch (V.currentLength = s - o,
                        V.startDate = i[o].date,
                        V.endDate = i[s - 1].date,
                        a.pcm) {
                        case 1:
                            h.prevclose = i[0].prevclose;
                            break;
                        case 2:
                            h.prevclose = i[o].close;
                            break;
                        default:
                            h.prevclose = o > 1 ? i[o - 1].close : i[0].prevclose || i[0].close
                        }
                        h.datas = i.slice(o, s),
                        h.dataLen = h.datas.length,
                        e(),
                        t(n)
                    }
                }
            }
              , F = new function() {
                var o, s = function(e) {
                    return o ? (e.volume = e.totalVolume - (o.totalVolume || 0),
                    e.amount = e.volume * e.price) : (o = {},
                    e.volume = 0),
                    o.totalVolume = e.totalVolume,
                    e.avg_price = e.totalAmount / e.totalVolume || e.price,
                    !0
                }, r = !1, l = function(e, n, a) {
                    if (e.isUpdateTime) {
                        var i = x.get(n);
                        if (i && !(i.length < 1)) {
                            var o = n == _.URLHASH.KD || n == _.URLHASH.KDF || n == _.URLHASH.KCL || n == _.URLHASH.KCLF
                              , s = i[i.length - 1];
                            if (1 == a) {
                                if (s.time && !t.kUtil.spk(s.time, e.time, b, n, h.market)) {
                                    if (t.kUtil.nc(i, e, n, {
                                        price: e.price,
                                        volume: e.volume
                                    }),
                                    /^forex|^BTC/.test(h.market))
                                        n == _.URLHASH.K1 && (s = i[i.length - 1],
                                        s.prevclose = e.prevclose,
                                        s.change = e.price - e.prevclose,
                                        s.percent = s.change / e.prevclose);
                                    else if ("NF" == h.market)
                                        ;
                                    else if (t.kUtil.spk("09:35", e.time, b, n)) {
                                        if (n == _.URLHASH.K60) {
                                            var l = e.time.split(":")
                                              , c = l[0]
                                              , d = l[1];
                                            if (c > 10 || 10 == c && d > 30)
                                                return
                                        }
                                        s = i[i.length - 1],
                                        s.open = e.open,
                                        s.open > s.high && (s.high = s.open),
                                        s.open < s.low && (s.low = s.open)
                                    }
                                    return
                                }
                            } else if (2 == a) {
                                if (!e.trstr)
                                    return;
                                t.kUtil.nc(i, e, n, {
                                    price: e.price,
                                    volume: 0
                                })
                            } else if (f(e.date, s.date))
                                h.nco && ("NF" == h.market ? m.dst(s.date) < h.nco.open && e.time >= h.nco.open && e.time > h.nco.close && t.kUtil.nc(i, e, n, null) : r && e.time >= h.nco.open && (r = !1,
                                t.kUtil.nc(i, e, n, null)));
                            else {
                                if (!(e.date > s.date))
                                    return;
                                h.nco ? "NF" == h.market ? e.time >= h.nco.open && t.kUtil.nc(i, e, n, null) : e.time <= h.nco.close && (r = !0) : t.kUtil.nc(i, e, n, null)
                            }
                            s = i[i.length - 1],
                            s.close = e.price,
                            s.date = m.ddt(e.date),
                            s.day = m.ds(s.date, "/"),
                            n == _.URLHASH.KMS ? (s.volume = e.trvolume || 0,
                            s.amount = e.tramount || 0,
                            s.trbs = e.trbs,
                            s.kke_cs = 0 == e.trbs ? -1 : 1) : (o ? (s.open = e.open,
                            s.high = e.high,
                            s.low = e.low,
                            s.volume = e.totalVolume) : isNaN(s.volume) ? s.volume = e.volume : s.volume += Number(e.volume),
                            s.kke_cs = s.close > s.open ? 1 : s.open > s.close ? -1 : 0);
                            var u;
                            1 == i.length ? u = o ? e.prevclose : s.open : (u = i[i.length - 2].close,
                            e.settlement && o && (u = e.settlement)),
                            /^forex|^BTC/.test(h.market) && (n == _.URLHASH.K1 || n == _.URLHASH.KD) && (u = e.prevclose),
                            s.change = e.price - u,
                            s.percent = s.change / Math.abs(u),
                            e.price > s.high && (s.high = e.price),
                            e.price < s.low && (s.low = e.price),
                            s.amplitude = Math.abs(s.high - s.low),
                            s.ampP = Math.abs(s.amplitude / u),
                            s.time = e.time,
                            t.isCNK(e.symbol) && (s.postVol = e.postVolume,
                            s.postAmt = e.postAmount),
                            ("G" == e.KCBType || "GC" == e.KCBType) && (s.postVol = e.postVolume,
                            s.postAmt = e.postAmount)
                        }
                    }
                }, c = function(e) {
                    l(e, _.URLHASH.KD, 0),
                    l(e, _.URLHASH.KW, 0),
                    l(e, _.URLHASH.KM, 0),
                    l(e, _.URLHASH.KY, 0),
                    l(e, _.URLHASH.KDF, 0),
                    l(e, _.URLHASH.KWF, 0),
                    l(e, _.URLHASH.KMF, 0),
                    l(e, _.URLHASH.KYF, 0),
                    l(e, _.URLHASH.KCL, 0),
                    l(e, _.URLHASH.KCLF, 0),
                    l(e, _.URLHASH.K1, 1),
                    l(e, _.URLHASH.K5, 1),
                    l(e, _.URLHASH.K15, 1),
                    l(e, _.URLHASH.K30, 1),
                    l(e, _.URLHASH.K60, 1),
                    l(e, _.URLHASH.K240, 1),
                    l(e, _.URLHASH.KMS, 2)
                }, d = new function() {
                    this.check = function(e) {
                        if (n)
                            return !0;
                        var a = V.viewId
                          , i = K.get(a);
                        if (!i || i.length < 1)
                            return !1;
                        var o = i[i.length - 1];
                        if (e.date > o.date)
                            if ("mink" == _.URLHASH.gt(V.viewId).type) {
                                if (!t.kUtil.spk(o.time, e.time, "00:00", a, h.market))
                                    return !1
                            } else if (!f(e.date, o.date))
                                return !1;
                        return !0
                    }
                }
                ;
                this.uUpdate = function(n, o, r, l) {
                    var u, p = {
                        symbol: e.symbol,
                        ssl: a.ssl
                    };
                    r ? (u = "datas.hq.parse",
                    p.hqStr = r,
                    p.market = l) : (u = "datas.hq.get",
                    p.delay = !0,
                    p.cancelEtag = o),
                    KKE.api(u, p, function(a) {
                        var o = a.dataObj[e.symbol];
                        if (o && o.date && s(o)) {
                            if (I = I || o.name || "",
                            !d.check(o))
                                return;
                            h.hq = o,
                            c(o),
                            i(!0),
                            t.isFunc(n) && n()
                        }
                    })
                }
            }
              , $ = new function() {
                var i, o = function(e, n) {
                    M.re(_.e.K_DATA_LOADED, n),
                    t.isFunc(e) && e()
                }, s = function(e) {
                    if (!h.hq || !h.hq.date)
                        return null;
                    var t = 0
                      , n = e.length - 1;
                    for (e[n].f || (e[n].f = 1); !e[t].f; )
                        t++;
                    return {
                        factor: e[t].f
                    }
                }, r = function(e, a, i, o) {
                    if (e) {
                        var s, r, l, c, h, d, u, p, f, v, g, b, y = !(-828 === e), N = x.getOriDK(), w = 0;
                        if (r = "q" === i ? _.URLHASH.KDF : _.URLHASH.KDB,
                        x.initState(r, t.clone(N, null), !1, !1, !0),
                        s = x.get(r),
                        b = s.length,
                        y) {
                            for (g = b - 1; g >= 0; g--) {
                                for (p = s[g],
                                f = m.ds(p.date); f < a[w].d; )
                                    w++;
                                if (v = Number(a[w].f),
                                "HK" === o) {
                                    if (p.high *= v,
                                    p.low *= v,
                                    p.open *= v,
                                    p.close *= v,
                                    "h" === i) {
                                        var k = Number(a[w].c);
                                        p.high += k,
                                        p.low += k,
                                        p.open += k,
                                        p.close += k
                                    }
                                } else if ("US" === o) {
                                    var S = Number(a[w].c) || 0;
                                    p.high = p.high * v + S,
                                    p.low = p.low * v + S,
                                    p.open = p.open * v + S,
                                    p.close = p.close * v + S
                                } else
                                    "h" === i ? (p.high *= v,
                                    p.low *= v,
                                    p.open *= v,
                                    p.close *= v) : (p.high /= v,
                                    p.low /= v,
                                    p.open /= v,
                                    p.close /= v)
                            }
                            for (g = 0; b > g; g++)
                                p = s[g],
                                v = Number(a[a.length - 1].f),
                                0 == g && (d = p.prevclose,
                                isNaN(d) || 0 >= d ? d = p.open : (d = "HK" === o ? p.prevclose * v : "h" === i ? p.prevclose * v : p.prevclose / v,
                                p.prevclose = d)),
                                p.amplitude = Math.abs(p.high - p.low),
                                p.ampP = Math.abs(p.amplitude / d),
                                p.change = p.close - d,
                                p.percent = p.change / Math.abs(d),
                                d = p.close
                        }
                        var M;
                        1 == b && (p = s[b - 1],
                        M = {
                            open: p.open,
                            high: p.high,
                            low: p.low,
                            close: p.close,
                            price: p.close,
                            volume: p.volume,
                            totalVolume: p.volume,
                            date: m.dd(p.date)
                        }),
                        l = t.kUtil.mw(s, M, null, null, 0 / 0),
                        h = l[0],
                        c = l[1],
                        u = l[2],
                        t.kUtil.pd(h, null),
                        t.kUtil.pd(c, null),
                        t.kUtil.pd(u, null),
                        x.initState(_.URLHASH["q" == i ? "KWF" : "KWB"], h),
                        x.initState(_.URLHASH["q" == i ? "KMF" : "KMB"], c),
                        x.initState(_.URLHASH["q" == i ? "KYF" : "KYB"], u);
                        var L = t.clone(s, null);
                        x.initState(_.URLHASH["q" == i ? "KCLF" : "KCLB"], L, !1, !0),
                        n || x.initState(r, s)
                    }
                }, l = function(t) {
                    var n = _.URLHASH.gt(V.viewId)
                      , i = n.dir
                      , l = {
                        symbol: e.symbol,
                        market: u,
                        dir: i,
                        ssl: a.ssl
                    };
                    P.show(),
                    KKE.api("datas.k.loadReData", l, function(e) {
                        P.hide();
                        var n = !0
                          , a = e.data;
                        if (a) {
                            var c = s(a);
                            c && (n = !1,
                            r(c.factor, a, i, l.market))
                        }
                        n && r(-828, null, i),
                        o(t, {
                            viewId: V.viewId
                        })
                    })
                }, c = function(e, t) {
                    var s = _.URLHASH.gt(i)
                      , r = "mink" == s.type ? x.initState : x.initDWMState;
                    P.show(),
                    "LSE" === u && (e.symbol = a.rawSymbol),
                    KKE.api("datas.k.get", e, function(l) {
                        P.hide();
                        var c = i;
                        if (i = 0 / 0,
                        "error" == l.msg) {
                            if (h.isErr = !0,
                            n)
                                if (l.data && l.data.hq) {
                                    var d;
                                    if (l.data.hq.status)
                                        switch (l.data.hq.status) {
                                        case 2:
                                            d = _.notlisted;
                                            break;
                                        case 3:
                                            d = _.delisted
                                        }
                                    else
                                        d = _.norecord;
                                    d && Y.showTip({
                                        txt: d,
                                        parent: C,
                                        noBtn: !0
                                    })
                                } else
                                    Y.showTip({
                                        txt: _.nodata,
                                        parent: C
                                    })
                        } else
                            l.data.hq && (h.hq = l.data.hq),
                            l.data.hq && (a.hq = l.data.hq),
                            r(s.baseid, l.data, e.ismink);
                        o(t, {
                            viewId: c
                        })
                    })
                }, d = function(t) {
                    KKE.api("datas.hq.get", {
                        symbol: e.symbol,
                        cancelEtag: !0,
                        ssl: a.ssl
                    }, function(n) {
                        var a = n.dataObj[e.symbol]
                          , i = [{
                            close: a.price,
                            open: a.open,
                            high: a.high,
                            low: a.low,
                            volume: 0,
                            prevclose: a.prevclose,
                            amplitude: Math.abs(a.high - a.low),
                            ampP: Math.abs((a.high - a.low) / a.prevclose),
                            change: a.price - a.prevclose,
                            date: a.date,
                            day: m.ds(a.date, "/"),
                            time: a.time,
                            percent: a.price - a.prevclose / a.prevclose,
                            kke_cs: 0
                        }];
                        x.initState(V.viewId, i, !0),
                        o(t, {
                            viewId: V.viewId
                        })
                    })
                }, p = function(t) {
                    var n, i, o = V.viewId, s = _.URLHASH.gt(o);
                    if (h.nco && h.nco.open)
                        i = h.nco.open,
                        b = i;
                    else {
                        var r = new Date
                          , l = b.split(":");
                        r.setHours(l[0], l[1], 0),
                        r.setMinutes(r.getMinutes() - 30),
                        i = m.dst(r)
                    }
                    var d = {
                        symbol: e.symbol,
                        newthour: i,
                        ssl: a.ssl
                    };
                    if ("mink" == s.type) {
                        if (n = e.datas.min,
                        d.ismink = !0,
                        d.scale = o,
                        /^forex|^BTC/.test(h.market))
                            switch (d.withsymbol = "sys_time",
                            o) {
                            case _.URLHASH.K1:
                                d.datalen = 1440;
                                break;
                            case _.URLHASH.K240:
                                d.datalen = parseInt(60 / o * 24 * 10);
                                break;
                            default:
                                d.datalen = parseInt(60 / o * 24 * 5)
                            }
                    } else
                        n = e.datas.day;
                    d.dataurl = n.url,
                    d.dataformatter = n.dataformatter,
                    d.wfn = n.wfn,
                    d.staticdata = n.staticdata,
                    c(d, t)
                }, f = function(e) {
                    h.nco = {
                        open: "20:00",
                        close: "15:30"
                    },
                    p(e)
                }, v = function(e) {
                    h.nco = {
                        open: "07:00",
                        close: "06:00"
                    },
                    p(e)
                }, g = function(t) {
                    var n = {
                        symbol: e.symbol,
                        ssl: a.ssl
                    }
                      , i = "datas.k.";
                    i += "loadGBInit",
                    h.nco = {
                        open: "15:00",
                        close: "23:30"
                    },
                    KKE.api(i, n, function(e) {
                        var n = e.data;
                        if (n) {
                            var a = n.time;
                            a && a.length > 0 && (h.nco.open = a[0][0] || h.nco.open,
                            h.nco.close = a[a.length - 1][1] || h.nco.close)
                        }
                        p(t)
                    })
                }, y = function(t, n) {
                    var i = {
                        symbol: e.symbol,
                        ssl: a.ssl
                    }
                      , o = "datas.k.";
                    n ? (o += "loadNFInit",
                    h.nco = {
                        open: "09:00",
                        close: "15:00"
                    }) : (o += "loadHFInit",
                    h.nco = {
                        open: "06:00",
                        close: "05:59"
                    }),
                    KKE.api(o, i, function(e) {
                        var n = e.data;
                        if (n) {
                            var a = n.time;
                            a && a.length > 0 && (h.nco.open = a[0][0] || h.nco.open,
                            h.nco.close = a[a.length - 1][1] || h.nco.close)
                        }
                        p(t)
                    })
                }, N = function(e, t) {
                    var n = new Date
                      , a = b.split(":");
                    n.setHours(a[0], a[1], 0),
                    n.setMinutes(n.getMinutes() - 1);
                    var i = m.dst(n);
                    h.nco = {
                        open: b,
                        close: i
                    },
                    "rek" == t.type && x.get(_.URLHASH.KD) ? l(e) : p(e)
                };
                this.iInit = function(e) {
                    var t = V.viewId;
                    if (i != t) {
                        i = t;
                        var n = _.URLHASH.gt(t);
                        switch (h.market) {
                        case "HF":
                            y(e);
                            break;
                        case "NF":
                            y(e, !0);
                            break;
                        case "global_index":
                            g(e);
                            break;
                        case "GOODS":
                            f(e);
                            break;
                        case "MSCI":
                            v(e);
                            break;
                        case "forex":
                        case "forex_yt":
                        case "BTC":
                            N(e, n);
                            break;
                        default:
                            "msk" == n.type ? d(e) : "rek" == n.type && x.get(_.URLHASH.KD) ? l(e) : p(e)
                        }
                    }
                }
            }
            ;
            this.kDb = x,
            this.extraDataObj = x.extraDataObj,
            this.getYtdIndex = function(e) {
                var t = x.get(_.URLHASH.KD);
                if (!t)
                    return null;
                var n = t[t.length - 1]
                  , a = n.date.getFullYear()
                  , i = 0;
                return e && (a--,
                i = n.date.getMonth()),
                l(new Date(a,i,1))
            }
            ,
            this.initData = $.iInit,
            this.doUpdate = F.uUpdate,
            this.onViewChange = i,
            this.setPricePos = function(e, t) {
                h.labelMaxP = e[0],
                h.labelMinP = e[1],
                h.labelPriceCount = e[2],
                h.isCompare = t,
                O.createPlayingData(),
                N && N.setPricePos(e)
            }
            ,
            this.setRange = function(e) {
                O.setDataRange(),
                y && y.setDataRange(),
                N && N.setDataRange(),
                w && w.setDataRange(e)
            }
            ,
            this.draw = function() {
                S.draw(),
                y && y.allDraw(q.x),
                N && N.allDraw(q.x)
            }
            ,
            this.resize = function(e) {
                O.createPlayingData(),
                S.resize(),
                y && y.onResize(e),
                N && N.onResize(),
                w && w.onResize()
            }
            ,
            this.clear = function(e) {
                S.clear(e),
                y && (y.clear(),
                y = null),
                N && (N.clear(),
                N = null),
                w && (w.clear(),
                w = null),
                n && (E = null)
            }
            ,
            this.getPriceTech = function() {
                return N || null
            }
            ;
            var G = function(e, n, a) {
                e && j.resizeAll(!0),
                A.onChangeView(),
                n && t.isFunc(n.callback) && n.callback(),
                a && z.onTechChanged(a[0])
            }
              , W = void 0;
            this.initPt = function(e, i) {
                if (e) {
                    !t.isArr(e) && (e = [e]);
                    for (var o = e.length; o--; )
                        if (e[o].name && "VOLUME" === e[o].name.toUpperCase()) {
                            e.splice(o, 1),
                            L.custom.show_underlay_vol = !0;
                            break
                        }
                    N || (N = new s({
                        iMgr: B,
                        stockData: h,
                        chartArea: R,
                        titleArea: D,
                        cb: G,
                        cfg: L,
                        type: "k",
                        usrObj: a
                    }),
                    n && (U = N),
                    W && (g = N.showHide(W),
                    W = void 0)),
                    N.createChart(e, i)
                }
            }
            ,
            this.removePt = function(e) {
                if (e) {
                    !t.isArr(e) && (e = [e]);
                    for (var n = e.length; n--; )
                        if (e[n].name && "VOLUME" === e[n].name.toUpperCase()) {
                            e.splice(n, 1),
                            L.custom.show_underlay_vol = !1;
                            break
                        }
                } else
                    L.custom.show_underlay_vol = !1;
                N && N.removeChart(e)
            }
            ,
            this.togglePt = function(e, t) {
                N ? g = N.showHide(e) : !t && (W = e)
            }
            ,
            this.initTc = function(e, t) {
                y || (y = new r({
                    stockData: h,
                    iMgr: B,
                    cb: G,
                    subArea: H,
                    cfg: L,
                    type: "k",
                    usrObj: a,
                    initMgr: j
                }),
                n && (T = y)),
                y.createChart(e, t)
            }
            ,
            this.removeTc = function(e) {
                y && y.removeChart(e)
            }
            ,
            this.initRs = function() {
                w = new o({
                    stockData: h,
                    setting: L,
                    rc: A.moving
                }),
                w.linkData(),
                E = w
            }
            ,
            this.setLineStyle = S.setLineStyle,
            this.getLineStyle = S.getLineStyle,
            c()
        }
        function k(e, a) {
            function i() {
                if (y)
                    r = L.COLOR.K_N,
                    s = L.COLOR.K_FALL,
                    l = L.COLOR.K_RISE,
                    c = L.COLOR.K_CL;
                else {
                    var a = o.linecolor
                      , i = a.K_N || "#" + t.randomColor();
                    r = i,
                    s = a.K_FALL || i,
                    l = a.K_RISE || i,
                    c = a.K_CL || i
                }
                m.K_N = r,
                m.K_FALL = s,
                m.K_RISE = l,
                m.K_CL = c,
                d = new n.xh5_ibPainter({
                    setting: L,
                    sd: e,
                    ctn: x,
                    withHBg: y,
                    fixScale: !1,
                    reO: {
                        mh: L.DIMENSION.H_MA4K
                    },
                    iMgr: B,
                    iTo: function(t, n, a, i) {
                        if (e && e.datas) {
                            !h(t, B.iHLineO.body) && t.appendChild(B.iHLineO.body);
                            var o = e.labelMaxP - a / L.DIMENSION.h_k * (e.labelMaxP - e.labelMinP);
                            B.iToD({
                                mark: o,
                                x: n,
                                y: a,
                                oy: L.DIMENSION.H_MA4K,
                                ox: L.DIMENSION.posX,
                                e: i
                            }, !0, !1)
                        }
                    }
                }),
                u = d.getG()
            }
            var o, s, r, l, c, d, u, m = {}, f = 1.3, v = 1.3, g = "solid", b = isNaN(a.nfloat) ? 2 : a.nfloat, y = e.isMain, N = function(e) {
                if (o = p({
                    linetype: "solid",
                    linecolor: m
                }, e || {}),
                m = o.linecolor,
                r = m.K_N,
                s = m.K_FALL,
                l = m.K_RISE,
                c = m.K_CL,
                !o.linetype && (o.linetype = g),
                L.datas.candle = o.linetype,
                0 == o.linetype.indexOf("line") || 0 == o.linetype.indexOf("mountain")) {
                    var t = Number(o.linetype.split("_")[1]);
                    (isNaN(t) || 0 >= t) && (t = v),
                    f = t
                }
            }, _ = function(t, n) {
                u.fillStyle = L.COLOR.K_EXT;
                for (var a, i, o, s = !1, r = !1, l = e.datas, c = l.length; c--; ) {
                    if (o = l[c],
                    a = n,
                    !s && o.high == e.rangeMax) {
                        s = !0;
                        var h = o.high.toFixed(b);
                        99 > a ? u.textAlign = "left" : a > L.DIMENSION.w_k - 99 ? (u.textAlign = "right",
                        a -= 5) : u.textAlign = "center",
                        i = o.hy,
                        i < L.STYLE.FONT_SIZE && (i = L.STYLE.FONT_SIZE + 2),
                        u.fillText(h, a, i)
                    }
                    if (a = n,
                    !r && o.low == e.rangeMin) {
                        r = !0;
                        var d = o.low.toFixed(b);
                        99 > a ? u.textAlign = "left" : a > L.DIMENSION.w_k - 99 ? (u.textAlign = "right",
                        a -= 5) : u.textAlign = "center",
                        i = Math.floor(o.ly + L.STYLE.FONT_SIZE + 2),
                        i > L.DIMENSION.h_k + .5 * L.STYLE.FONT_SIZE - 3 && (i = L.DIMENSION.h_k),
                        u.fillText(d, a, i)
                    }
                    if (r && s)
                        break;
                    n -= t,
                    0 > n && (n = 0)
                }
            }, w = function() {
                var t = e.datas
                  , n = t.length
                  , a = L.DIMENSION.w_k / Math.max(n, L.PARAM.minCandleNum)
                  , i = .5 * a
                  , o = q.x - a;
                d.beginPath();
                for (var s, r, l = 0; n > l; l++)
                    s = t[l],
                    r = s.vy,
                    d.drawVStickC(o, r, i, L.DIMENSION.h_k, L.COLOR.V_SD),
                    o += a;
                d.stroke()
            }, k = function() {
                for (var t, n, a = e.datas, i = a.length, s = L.DIMENSION.w_k / Math.max(i, L.PARAM.minCandleNum), r = q.x - .4 * s, l = 0; i > l; l++)
                    n = a[l],
                    t = n.cy,
                    0 == l ? (d.newStyle(c, !0, f),
                    d.moveTo(r, t)) : d.lineTo(r, t),
                    n.ix = r,
                    r += s;
                d.stroke(),
                0 == o.linetype.indexOf("mountain") && (r -= s,
                d.lineTo(r, L.DIMENSION.h_k),
                d.lineTo(q.x - .4 * s, L.DIMENSION.h_k),
                d.newFillStyle_rgba(L.COLOR.M_ARR, L.DIMENSION.h_k, L.COLOR.M_ARR_A),
                d.fill()),
                y && L.custom.show_ext_marks && _(s, r)
            }, S = function() {
                for (var t, n, a, i, o = e.datas, c = o.length, h = L.DIMENSION.w_k / Math.max(c, L.PARAM.minCandleNum), u = .6 * h, p = -1, m = 1, f = 0; 3 > f; f++) {
                    switch (p) {
                    case -1:
                        i = s;
                        break;
                    case 0:
                        i = r;
                        break;
                    case 1:
                        i = l
                    }
                    for (t = q.x - h,
                    d.beginPath(),
                    a = 0; c > a; a++)
                        n = o[a],
                        n.isFake || (n.kke_cs == p && d.drawCandleRect(t, n.oy, n.cy, u, i, n.kke_cs == m),
                        0 == f && (n.ix = t + u)),
                        t += h;
                    for (d.stroke(),
                    t = q.x - h,
                    d.beginPath(),
                    a = 0; c > a; a++)
                        n = o[a],
                        n.isFake || n.kke_cs == p && d.drawCandleLineRect(t, n.hy, n.oy, n.cy, n.ly, u, i, n.kke_cs == m),
                        t += h;
                    d.stroke(),
                    p++
                }
                y && L.custom.show_ext_marks && _(h, t)
            }, M = function() {
                var t, n, a, i = e.datas, o = i.length, c = L.DIMENSION.w_k / Math.max(o, L.PARAM.minCandleNum), h = .6 * c, u = -1;
                h = Math.floor(h) % 2 === 0 ? Math.floor(h) : Math.floor(h) - 1;
                for (var p, m = 0; 3 > m; m++) {
                    switch (u) {
                    case -1:
                        p = s;
                        break;
                    case 0:
                        p = r;
                        break;
                    case 1:
                        p = l
                    }
                    for (t = q.x - c,
                    d.beginPath(),
                    a = 0; o > a; a++)
                        n = i[a],
                        n.isFake || (n.kke_cs == u && d.drawCandleRect_solid(t, n.oy, n.cy, h, p),
                        0 == m && (n.ix = t + h)),
                        t += c;
                    for (d.stroke(),
                    t = q.x - c,
                    d.beginPath(),
                    a = 0; o > a; a++)
                        n = i[a],
                        n.isFake || n.kke_cs == u && d.drawCandleLineRect(t, n.hy, n.oy, n.cy, n.ly, h, p, !1),
                        t += c;
                    d.stroke(),
                    u++
                }
                y && L.custom.show_ext_marks && _(c, t)
            }, A = function() {
                for (var t, n, a, i, o = e.datas, c = o.length, h = L.DIMENSION.w_k / Math.max(c, L.PARAM.minCandleNum), u = .6 * h, p = -1, m = 0; 3 > m; m++) {
                    switch (p) {
                    case -1:
                        i = s;
                        break;
                    case 0:
                        i = r;
                        break;
                    case 1:
                        i = l
                    }
                    for (t = q.x - h,
                    d.beginPath(),
                    a = 0; c > a; a++)
                        n = o[a],
                        n.isFake || (0 == m && (n.ix = t + u),
                        n.kke_cs == p && d.drawOhlc(t, n.oy, n.hy, n.ly, n.cy, u, i)),
                        t += h;
                    d.stroke(),
                    p++
                }
                y && L.custom.show_ext_marks && _(h, t)
            }, I = function() {
                y && d.drawBg(q.x);
                var t = e.datas;
                if (t) {
                    var n = 0 == o.linetype.indexOf("line") || 0 == o.linetype.indexOf("mountain")
                      , a = 0 == o.linetype.indexOf("hollow")
                      , i = 0 == o.linetype.indexOf("ohlc");
                    d.clear(n, L.PARAM.getHd()),
                    d.newGStyle({
                        textBaseline: "bottom",
                        font: L.STYLE.FONT_SIZE + "px " + L.STYLE.FONT_FAMILY
                    }),
                    y && L.custom.show_underlay_vol && w(),
                    n ? k() : a ? S() : i ? A() : M(),
                    L.custom.show_k_gap && C()
                }
            }, C = function() {
                for (var t = [], n = e.datas, a = n[n.length - 1], i = a.ly, o = a.hy, s = a.low, r = a.high, l = n.length - 1; l--; )
                    a = n[l],
                    a.ly < o ? t.push({
                        x: a.ix,
                        upper: a.ly,
                        lower: o,
                        p1: a.low,
                        p2: r,
                        type: "fall"
                    }) : a.hy > i && t.push({
                        x: a.ix,
                        upper: i,
                        lower: a.hy,
                        p1: a.high,
                        p2: s,
                        type: "rise"
                    }),
                    a.hy < o && (o = a.hy),
                    a.ly > i && (i = a.ly),
                    a.high > r && (r = a.high),
                    a.low < s && (s = a.low);
                d.beginPath(),
                u.globalCompositeOperation = "destination-over";
                for (var c, h = 0, p = Math.min(t.length, L.PARAM.gapNum); p > h; h++)
                    c = t[h],
                    d.drawRect(c.x, c.upper, c.lower, L.DIMENSION.w_k, L.COLOR.K_GAP);
                if (L.custom.show_k_gap_price) {
                    u.globalCompositeOperation = "source-over";
                    for (var c, h = 0, p = Math.min(t.length, L.PARAM.gapNum); p > h; h++)
                        c = t[h],
                        d.drawTxt([c.p1, c.p2].join("~"), c.x, c.upper, {
                            color: L.COLOR.K_GAP_TXT
                        }, L.DIMENSION.w_k)
                }
            };
            this.draw = I,
            this.clear = function(e) {
                e ? d.clear(!1, L.PARAM.getHd()) : (d.remove(),
                d = null)
            }
            ,
            this.resize = function() {
                d.resize({
                    mh: L.DIMENSION.H_MA4K
                }),
                I()
            }
            ,
            this.setLineStyle = N,
            this.getLineStyle = function() {
                return o
            }
            ,
            N(a),
            i()
        }
        function S() {
            var e, n, l, h, d = this, f = [], g = .05, y = function() {
                var e, t, n = Number.MAX_VALUE, i = -Number.MAX_VALUE, o = f.length, s = o > 1 || "percent" == L.datas.scaleType;
                L.custom.k_overlay && (s = !1);
                for (var r, l, c, h, d = s ? "Percent" : "Price", u = o; u--; )
                    e = f[u],
                    a.scalerange ? c = a.scalerange : (h = e.getPriceTech(),
                    s || !h ? c = [i, n] : (t = h && h.getMaxMin(),
                    c = t || [i, n])),
                    r = e["min" + d],
                    l = e["max" + d],
                    isFinite(r) && isFinite(l) && (n = Math.min(n, r, c[1]),
                    i = Math.max(i, l, c[0]));
                var p;
                p = a.scalerange ? a.scalerange.concat(4) : 1 == a.pcm ? .0199 > i - n ? [i, n, 1] : v(i, n, 2, !1, !0) : v(i, n, a.nfloat, !1, !0, g);
                for (var m = o; m--; )
                    e = f[m],
                    e.setPricePos(p, s)
            }, N = function() {
                (V.start < 1 || !L.custom.smooth) && q.resetX();
                for (var e = f.length; e--; )
                    f[e].draw()
            }, w = function() {
                V.start = V.end = 0 / 0,
                V.currentLength = 0 / 0,
                n = void 0
            }, k = function(t) {
                w();
                for (var n, a = f.length, i = 0; a > i; i++)
                    n = f[i],
                    n.onViewChange();
                y(),
                N(),
                t || z.onRange(e, a > 1)
            }, S = [], M = !1, A = function(t) {
                return t.isErr ? (t !== e && d.removeCompare([t.symbol]),
                !0) : t.kDb.get() ? !0 : (t.initData(R),
                !1)
            }, I = function(e) {
                if (e && t.isFunc(e.callback)) {
                    for (var n = !1, a = S.length; a--; )
                        if (e.callback === S[a]) {
                            n = !0;
                            break
                        }
                    !n && S.push(e.callback)
                }
            }, x = function() {
                for (var t, n = !0, a = f.length; a--; )
                    t = f[a],
                    t == e || A(t) || (n = !1,
                    M = !0);
                return n
            }, R = function(t, n) {
                if (I(n),
                A(e)) {
                    if (e.isErr)
                        return void (e.isErr = !1);
                    if (B.patcher.switchFloater(),
                    q.resetX(0),
                    x())
                        for (M = !1,
                        k(t); S.length; ) {
                            var a = S.shift();
                            a()
                        }
                    if (z.onViewChanged(),
                    t)
                        return;
                    z.onDataUpdate(),
                    z.onViewPrice()
                }
            }, D = function(t) {
                (t || n && V.dataLength != n) && z.onRange(e, f.length > 1),
                n = V.dataLength
            }, H = function(e) {
                (e || V.end == V.dataLength) && (B.update(),
                y(),
                N(),
                D(!0)),
                z.onDataUpdate(),
                !B.isIng() && z.onViewPrice()
            }, K = function(e) {
                clearTimeout(h),
                !F && C.parentNode && "none" != C.style.display && (h = setTimeout(H, e || 200))
            }, T = function() {
                if (!M)
                    for (var e, t = f.length; t--; )
                        e = f[t],
                        e.doUpdate(K)
            }, U = function() {
                if (clearInterval(l),
                !isNaN(a.rate)) {
                    var e = 1e3 * a.rate;
                    e > 0 && (l = setTimeout(U, e))
                }
                T()
            };
            this.mM = new function() {
                var n = function(a, i, o) {
                    var l, c;
                    switch (i) {
                    case "price":
                        if (l = s,
                        c = "initPt",
                        t.isObj(a))
                            (a.name && "TZY" === String(a.name).toUpperCase() || a.name && "BS" === String(a.name).toUpperCase()) && (g = .2);
                        else if (t.isArr(a))
                            for (var h, d = a.length; d--; )
                                if (h = a[d],
                                h && h.name && ("TZY" === String(h.name).toUpperCase() || "BS" === String(h.name).toUpperCase())) {
                                    g = .2;
                                    break
                                }
                        break;
                    case "tech":
                        l = r,
                        c = "initTc"
                    }
                    c && (l ? e[c](a, o) : KKE.api("plugins.techcharts.get", {
                        type: i
                    }, function(e) {
                        r = e.tChart,
                        s = e.pChart,
                        n(a, i, o)
                    }))
                }
                  , a = function(t, n) {
                    var a;
                    switch (n) {
                    case "price":
                        a = "removePt",
                        g = .05;
                        break;
                    case "tech":
                        a = "removeTc";
                        break;
                    default:
                        return
                    }
                    e && e[a](t)
                }
                  , i = function(t) {
                    return o ? (E ? (E.sh(t),
                    (t.from || t.to) && E.dateFromTo(t.from, t.to)) : (e.initRs(),
                    i(t),
                    O.appendChild(E.getBody())),
                    void j.resizeAll(!0)) : void KKE.api("plugins.rangeselector.get", null, function(e) {
                        o = e,
                        i(t)
                    })
                };
                this.showRs = i,
                this.newAC = n,
                this.removeAC = a,
                this.togglePt = function(t, n) {
                    e && (e.togglePt(t, n),
                    R())
                }
            }
            ;
            var P = new function() {
                var n, i, o, s, r = !1, l = !1, h = function() {
                    i || (i = c("div"),
                    i.style.margin = "0 auto"),
                    i.style.width = .8 * L.DIMENSION.getStageW() + "px",
                    i.style.height = .83 * L.DIMENSION.h_k + "px"
                }, d = function(e) {
                    n.dateTo(e.date, function(e) {
                        1 != e && Y.showTip({
                            txt: _.nohistoryt,
                            parent: C
                        })
                    })
                }, u = function(t) {
                    if (o && n) {
                        l = !0;
                        var a = n.getSymbols()[0];
                        a != e.symbol && n.newSymbol({
                            symbol: e.symbol
                        }),
                        n.resize(),
                        d(t),
                        n.show(i)
                    }
                }, p = function() {
                    l = !1
                }, f = function(n) {
                    var a = {
                        txt: e.getName() + "(" + e.symbol + ") " + m.ds(n.date),
                        content: i,
                        parent: C,
                        fontColor: "#000",
                        closeCb: p,
                        btnLb: "\u5173\u95ed",
                        bgStyle: {
                            backgroundColor: "#fff",
                            width: "80%",
                            top: "2%"
                        }
                    };
                    return o || (o = new t.TipM(L.COLOR)),
                    a.content = i,
                    a
                }, v = function(t) {
                    var s = f(t);
                    if (o.genTip(s),
                    n)
                        u(t);
                    else {
                        if (r)
                            return;
                        r = !0,
                        KKE.api("chart.h5t.get", {
                            symbol: e.symbol,
                            dom: i,
                            nfloat: a.nfloat
                        }, function(e) {
                            n = e,
                            r = !1,
                            u(t)
                        })
                    }
                };
                this.resetHisT = function() {
                    o && o.hide()
                }
                ,
                this.isShowing = function() {
                    return l
                }
                ,
                this.historyT = function() {
                    if ("CN" === t.market(e.symbol)) {
                        s = B.getInteractiveIdx();
                        var n = e.datas[s];
                        if (n) {
                            if (n.date.getFullYear() < 2008)
                                return void Y.showTip({
                                    txt: _.historyt08,
                                    parent: C
                                });
                            switch (L.custom.history_t) {
                            case "layer":
                                h(),
                                v(n);
                                break;
                            case "window":
                                var a = "https://finance.sina.com.cn/h5charts/tchart.html?symbol=$symbol&date=$date&rangeselector=true&indicator=tvol";
                                a = a.replace("$symbol", e.symbol).replace("$date", m.ds(n.date));
                                var i = "width=600,height=375,location=0,menubar=0,titlebar=0,toolbar=0,alwaysRaised=1";
                                window.open(a, "_blank", i);
                                break;
                            default:
                                return
                            }
                        }
                    }
                }
            }
            ;
            this.h5tM = P,
            this.getAllStock = function() {
                return f
            }
            ,
            this.getMainStock = function() {
                return e
            }
            ,
            this.getAllSymbols = function() {
                for (var e = [], t = 0, n = f.length; n > t; t++)
                    e.push(f[t].symbol);
                return e
            }
            ;
            var $ = function() {
                d.mM.togglePt(f.length > 1 ? {
                    v: !1
                } : V.viewId == _.URLHASH.KCL || V.viewId == _.URLHASH.KCLF || V.viewId == _.URLHASH.KCLB ? {
                    v: !1
                } : {
                    v: !0
                })
            }
              , G = function(t, n, a, i, o) {
                if (!a && q.resetX(),
                !(n - t < L.PARAM.minCandleNum || n > V.dataLength || 0 > t || n - t > L.PARAM.maxCandleNum)) {
                    V.start = t,
                    V.end = n,
                    V.currentLength = n - t;
                    for (var s, r = f.length, l = 0; r > l; l++)
                        s = f[l],
                        s.setRange(i);
                    y(),
                    N(),
                    o || z.onRange(e, r > 1)
                }
            };
            this.onChangeView = R,
            this.showYTD = function(t, n) {
                V.viewId = _.URLHASH.KD + t,
                R(!0);
                var a = e.getYtdIndex(n);
                a && G(a[0], a[1] + 1)
            }
            ,
            this.moving = G,
            this.callSdDraw = N;
            var W = function(t, n) {
                var a = t instanceof i ? t : new i(t,n);
                n && (e = a),
                f.push(a),
                $(),
                R()
            }
              , X = function(n) {
                if ("mink" == _.URLHASH.gt(V.viewId).type) {
                    var a = t.market(n.symbol)
                      , i = t.market(e.symbol);
                    if (a != i && ("US" == a || "US" == i))
                        return !1
                }
                return !0
            };
            this.compare = function(e) {
                for (var n = e.callback, a = f.length; a--; )
                    if (f[a].symbol == e.symbol)
                        return void (t.isFunc(n) && n({
                            code: 1,
                            msg: "comparing same symbol"
                        }));
                X(e) ? W(e, !1) : t.isFunc(n) && n({
                    code: 2,
                    msg: "invalid comparing market or period"
                })
            }
            ,
            this.removeCompare = function(e, t) {
                for (var n, a, i = !1, o = e.length; o--; ) {
                    a = e[o];
                    for (var s = f.length; s--; )
                        if (a == f[s].symbol) {
                            i = !0,
                            n = f.splice(s, 1)[0],
                            n.clear(t),
                            n = null;
                            break
                        }
                }
                i && !t && ($(),
                y(),
                N())
            }
            ;
            var Z, J = function(e) {
                e ? H() : V.end == V.dataLength && B.update()
            }, Q = !1, ee = 0, te = function() {
                clearTimeout(Z),
                Q = !1,
                ee = 0
            }, ne = function() {
                Z = setTimeout(function() {
                    ee > 0 && K(1),
                    te()
                }, 500)
            };
            this.pushData = function(e, t) {
                var n = !1;
                switch (Number(t)) {
                case 0:
                    te();
                    break;
                case 1:
                    te(),
                    n = !0;
                    break;
                case 2:
                    Q || (Q = !0,
                    ne())
                }
                for (var a = e.length; a--; )
                    for (var i = f.length; i--; )
                        if (f[i].symbol === e[a].symbol && e[a].data) {
                            ee++,
                            f[i].doUpdate(b(J, null, n), !1, e[a].data, e[a].market);
                            break
                        }
            }
            ,
            this.setScale = function(e) {
                L.datas.scaleType = e,
                y(),
                N()
            }
            ,
            this.setLineStyle = function(n) {
                if (n) {
                    !t.isArr(n) && (n = [n]);
                    for (var a = n.length; a--; ) {
                        var i = n[a];
                        if (i.hasOwnProperty("symbol")) {
                            for (var o = i.symbol, s = f.length; s--; )
                                if (f[s].symbol == o) {
                                    f[s].setLineStyle(i),
                                    f[s].draw();
                                    break
                                }
                        } else
                            e.setLineStyle(i),
                            e.draw()
                    }
                } else
                    e.setLineStyle(),
                    e.draw()
            }
            ,
            this.onResize = function(e) {
                for (var t = f.length; t--; )
                    f[t].resize(e)
            }
            ;
            var ae = -1
              , ie = -1
              , oe = function(e, t) {
                var n = V.start
                  , a = V.end
                  , i = e / Math.abs(e)
                  , o = i * Math.ceil((a - n) / L.PARAM.zoomUnit);
                if (Math.abs(o) > L.PARAM.zoomLimit && (o = i * L.PARAM.zoomLimit),
                L.custom.centerZoom) {
                    var s = t ? t.layerX / L.DIMENSION.w_k : .5;
                    s < L.PARAM.zoomArea ? a = Math.min(a - o * Math.abs(o), V.dataLength) : s > 1 - L.PARAM.zoomArea ? n = Math.max(n + o * Math.abs(o), 0) : (n = Math.max(n + o * Math.abs(o), 0),
                    a = Math.min(a - o * Math.abs(o), V.dataLength))
                } else
                    n = Math.max(n + o * Math.abs(o), 0);
                return n == ae && a == ie ? [-1] : (ae = n,
                ie = a,
                [n, a])
            };
            this.onWheel = function(e) {
                if (!P.isShowing()) {
                    var t = e.detail || -1 * e.wheelDelta;
                    if (0 != t) {
                        var n = oe(t, e);
                        G(n[0], n[1])
                    }
                }
            }
            ,
            this.onKb = function(e) {
                if ("keyup" == e.type)
                    return void B.iToKb(null, !0);
                var t = e.keyCode;
                if (P.isShowing())
                    return void (27 == t && P.resetHisT());
                switch (t) {
                case 38:
                case 40:
                    var n = oe(38 == t ? 1 : -1);
                    G(n[0], n[1]);
                    break;
                case 37:
                case 39:
                    var a = B.iToKb(37 == t ? -1 : 1);
                    a && (G(V.start + a, V.end + a),
                    B.iToKb(0));
                    break;
                case 13:
                    P.historyT();
                    break;
                default:
                    return
                }
                u.preventDefault(e)
            }
            ,
            this.zoomApi = function(e) {
                var t = oe(e ? 1 : -1);
                G(t[0], t[1])
            }
            ,
            this.moveApi = function(e) {
                var t = V.start
                  , n = V.end;
                t += e,
                n += e,
                n > V.dataLength && (n = V.dataLength,
                t = V.start + n - V.end),
                0 > t && (t = 0,
                n = V.end - V.start),
                G(t, n)
            }
            ,
            this.shareTo = function(e) {
                e = p({
                    type: "weibo",
                    url: window.location.href,
                    wbtext: "",
                    qrwidth: 100,
                    qrheight: 100,
                    extra: void 0
                }, e || {});
                var n = String(e.type).toLowerCase();
                switch (n) {
                case "qrcode":
                    KKE.api("utils.qrcode.createcanvas", {
                        text: e.url,
                        width: e.qrwidth,
                        height: e.qrheight
                    }, function(e) {
                        Y.showTip({
                            content: e,
                            txt: '<p style="margin:0 0 9px 0;">\u626b\u63cf\u4e8c\u7ef4\u7801</p>',
                            parent: C,
                            btnLb: "\u5173\u95ed"
                        })
                    });
                    break;
                default:
                    t.grabM.shareTo({
                        ctn: C,
                        w: L.DIMENSION.getStageW(),
                        h: L.DIMENSION.getStageH() - (O.clientHeight || 0),
                        ignoreZIdxArr: [L.PARAM.I_Z_INDEX],
                        ignoreIdArr: [L.PARAM.LOGO_ID],
                        priorZIdx: L.PARAM.G_Z_INDEX,
                        nologo: !1,
                        top: L.DIMENSION.posY + L.DIMENSION.H_MA4K + 17,
                        right: L.DIMENSION.RIGHT_W + L.DIMENSION.K_RIGHT_W,
                        LOGO_W: L.DIMENSION.LOGO_W,
                        LOGO_H: L.DIMENSION.LOGO_H,
                        color: L.COLOR.LOGO,
                        bgColor: L.COLOR.BG,
                        txt: e.wbtext,
                        url: e.url,
                        extra: e.extra
                    })
                }
            }
            ,
            this.getExtraData = function(n) {
                if (n = p({
                    symbol: e.symbol,
                    name: null,
                    clone: !0
                }, n || {}),
                !n.name)
                    return null;
                for (var a, i, o = f.length; o--; )
                    if (f[o].symbol === n.symbol) {
                        a = f[o];
                        break
                    }
                if (a) {
                    var s;
                    "currentK" == n.name ? (s = a.kDb.get(),
                    i = n.clone ? t.clone(s, null) : s) : (s = a.extraDataObj[n.name],
                    i = n.clone ? t.clone(s, null) : s)
                }
                return i
            }
            ,
            this.updateDataAll = U,
            this.outputNewRange = D,
            this.dcReset = function() {
                clearInterval(l),
                clearTimeout(h);
                for (var e, t = f.length; t--; )
                    e = f.splice(t, 1)[0],
                    e.clear(),
                    e = null
            }
            ,
            this.dcInit = function(e) {
                W(e, !0),
                U()
            }
        }
        t.xh5_EvtDispatcher.call(this);
        var M = this;
        a = p({
            candlenum: 0 / 0,
            datas: {
                day: {
                    wfn: void 0,
                    url: void 0,
                    dataformatter: void 0,
                    staticdata: void 0
                },
                min: {
                    wfn: void 0,
                    url: void 0,
                    dataformatter: void 0,
                    staticdata: void 0
                }
            },
            dim: null,
            dom: void 0,
            domid: void 0,
            fh5: !1,
            maxcandlenum: 0 / 0,
            mincandlenum: 0 / 0,
            mh: 0,
            name: void 0,
            nfloat: 2,
            noh5: void 0,
            nohtml5info: void 0,
            ondataupdate: void 0,
            onrange: void 0,
            onviewchanged: void 0,
            onviewprice: void 0,
            ontechchanged: void 0,
            onshortclickmain: void 0,
            pcm: 0,
            rate: 0 / 0,
            reorder: !0,
            reheight: !0,
            scalerange: void 0,
            ssl: !0,
            symbol: "sh000001",
            tchartobject: {
                t: void 0,
                k: void 0
            },
            theme: null,
            trace: void 0,
            view: "kd",
            w: 0 / 0,
            h: 0 / 0,
            zoomlimit: 0 / 0,
            zoomunit: 0 / 0,
            hq: {}
        }, a || {
            WANGXuan: "wangxuan2@staff.sina.com.cn",
            VER: "2.11.1"
        });
        var L;
        !function() {
            if (!a.symbol && (a.symbol = "sh000001"),
            a.symbol = String(a.symbol),
            a.rawSymbol = String(a.symbol),
            a.symbol = "LSE" === t.market(a.symbol) ? t.strUtil.replaceStr(a.symbol) : a.symbol.replace(".", "$"),
            L = e.getSetting(["_", a.symbol, "_", Math.floor(1234567890 * Math.random() + 1) + Math.floor(9876543210 * Math.random() + 1)].join("")),
            0 == location.protocol.indexOf("https:") && (a.ssl = !0),
            isNaN(a.rate) && (a.rate = L.PARAM.updateRate),
            !isNaN(a.mincandlenum) && a.mincandlenum > 0 && (L.PARAM.minCandleNum = a.mincandlenum),
            !isNaN(a.candlenum) && a.candlenum >= L.PARAM.minCandleNum && (L.PARAM.defaultCandleNum = a.candlenum),
            isNaN(a.maxcandlenum) || (L.PARAM.maxCandleNum = a.maxcandlenum),
            !isNaN(a.zoomunit) && a.zoomunit > L.PARAM.minCandleNum && (L.PARAM.zoomUnit = a.zoomunit),
            !isNaN(a.zoomlimit) && a.zoomlimit > 0 && (L.PARAM.zoomLimit = Math.round(a.zoomlimit)),
            g.noH5) {
                if ("undefined" == typeof FlashCanvas || a.fh5)
                    return void (t.isFunc(a.noh5) && a.noh5(a));
                L.PARAM.isFlash = !0
            }
            if (L.PARAM.isFlash && (L.COLOR.F_BG = "#fff"),
            a.reorder || (L.custom.indicator_reorder = !1),
            a.reheight || (L.custom.indicator_reheight = !1),
            a.dim)
                for (var n in a.dim)
                    a.dim.hasOwnProperty(n) && t.isNum(L.DIMENSION[n]) && (L.DIMENSION[n] = a.dim[n]),
                    a.dim.hasOwnProperty(n) && t.isNum(L.STYLE[n]) && (L.STYLE[n] = a.dim[n])
        }();
        var A, I, C, x, R, D, H, O, K, T, U, E, P, F = !1, $ = 0, V = {
            viewId: _.URLHASH.vi(a.view || "kd"),
            dataLength: 0 / 0,
            start: 0 / 0,
            end: 0 / 0,
            currentLength: 0 / 0,
            startDate: void 0,
            endDate: void 0,
            movY: 0
        }, q = {
            x: 0,
            resetX: function(e) {
                this.x = isNaN(e) ? L.DIMENSION.w_k / Math.max(V.currentLength, L.PARAM.minCandleNum) : e
            }
        }, Y = new function() {
            var e;
            this.showTip = function(n) {
                e || (e = new t.TipM(L.COLOR)),
                e.genTip(n)
            }
            ,
            this.hideTip = function() {
                e && e.hide()
            }
        }
        , z = new function() {
            var e = function() {
                var e = K.get(V.viewId);
                return e ? e[e.length - 1] : null
            };
            this.onRange = function(e, n) {
                !F && t.isFunc(a.onrange) && a.onrange({
                    isCompare: n,
                    data: e.datas,
                    viewRangeState: t.clone(V, null),
                    width: L.DIMENSION.w_k,
                    height: L.DIMENSION.h_k,
                    left: L.DIMENSION.posX,
                    top: L.DIMENSION.H_MA4K,
                    range: [e.labelMaxP, e.labelMinP, e.labelMaxVol],
                    minCandleNum: L.PARAM.minCandleNum
                })
            }
            ;
            var n = [];
            this.onViewPrice = function(i, o, s, r, l, c) {
                if (!F && t.isFunc(a.onviewprice)) {
                    if (!i) {
                        if (i = e(),
                        !i)
                            return;
                        o = V.currentLength - 1
                    }
                    if (!s) {
                        for (; n.length; )
                            n.length--;
                        for (var h, d, u, p, m = A.getAllStock(), f = 0, v = m.length; v > f; f++)
                            p = m[f],
                            h = p.datas,
                            !h || h.length <= o || (d = p.getName(),
                            u = h[o],
                            !r && m[f].isMain && (r = h),
                            n.push({
                                name: d,
                                data: u,
                                rangedata: h,
                                symbol: p.symbol,
                                color: p.getLineStyle().linecolor
                            }));
                        s = n
                    }
                    l || (l = A.getMainStock().getName()),
                    a.onviewprice({
                        data: t.clone(i, null),
                        rangedata: r,
                        idx: o,
                        left: L.DIMENSION.posX,
                        top: L.DIMENSION.H_MA4K,
                        data_array: s,
                        curname: l,
                        interacting: !!c,
                        stockType: a.hq && a.hq.KCBType
                    })
                }
            }
            ,
            this.onDataUpdate = function() {
                if (t.isFunc(a.ondataupdate)) {
                    var n = e();
                    n && a.ondataupdate({
                        data: t.clone(n, null),
                        idx: V.currentLength - 1,
                        left: L.DIMENSION.posX,
                        top: L.DIMENSION.H_MA4K
                    })
                }
            }
            ,
            this.onViewChanged = function() {
                t.isFunc(a.onviewchanged) && a.onviewchanged({
                    viewRangeState: t.clone(V, null)
                })
            }
            ,
            this.onInnerResize = function(e) {
                t.isFunc(a.oninnerresize) && a.oninnerresize(e)
            }
            ,
            this.onTechChanged = function(e) {
                t.isFunc(a.ontechchanged) && a.ontechchanged({
                    Indicator: e
                })
            }
            ,
            this.shortClickHandler = function() {
                t.isFunc(a.onshortclickmain) && a.onshortclickmain()
            }
        }
        , j = new function() {
            var e, n, i, o, s, r = 37, h = function(e, t, n) {
                var i = !1;
                isNaN(e) && (e = a.w || I.offsetWidth),
                isNaN(t) && (t = a.h || I.offsetHeight - a.mh);
                for (var o, s = O.clientHeight || 0, r = H.clientHeight || 0, l = L.DIMENSION.getOneWholeTH(), c = 0, h = H.childNodes, d = h.length, u = 0, p = h.length; p--; )
                    o = h[p],
                    o.id.indexOf("blankctn") >= 0 ? (c = o.offsetHeight,
                    d--,
                    u += c) : u += l;
                return !isNaN(n) && (r -= n),
                r / (t - s) > 1 && (r = u,
                i = !0),
                L.DIMENSION.setStageW(e),
                1 == $ ? d > 0 && (L.DIMENSION.setStageH(t, d * l + c + s),
                i = !0,
                $ = 0) : L.DIMENSION.setStageH(t, r + s),
                i
            }, d = function() {
                s && (s.style.display = L.custom.show_logo ? "" : "none")
            }, p = function() {
                P = new t.LoadingSign,
                P.appendto(x)
            }, m = function() {
                P.setPosition()
            }, f = function(e, n, a) {
                var o = h(n, a, 0 / 0);
                if (e || n && a) {
                    if (!A)
                        return;
                    A.onResize(o),
                    B.onResize()
                }
                i.style.left = "1px",
                i.style.top = L.DIMENSION.h_k + L.DIMENSION.H_MA4K + "px",
                d(),
                m(),
                t.stc("k_wh", [L.DIMENSION.getStageW(), L.DIMENSION.getStageH()])
            }, v = function() {
                I = l(a.domid) || a.dom,
                I || (I = c("div")),
                C = c("div"),
                C.style.position = "relative",
                C.style.outlineStyle = "none",
                C.style.webkitUserSelect = C.style.userSelect = C.style.MozUserSelect = "none",
                x = c("div", "mainarea_" + L.uid),
                R = c("div"),
                x.appendChild(R),
                D = c("div"),
                D.style.position = "absolute",
                D.style.fontSize = L.STYLE.FONT_SIZE + "px",
                D.style.lineHeight = L.DIMENSION.H_MA4K + "px",
                D.style.width = "100%",
                x.appendChild(D),
                C.appendChild(x),
                H = c("div"),
                C.appendChild(H),
                O = c("div"),
                C.appendChild(O),
                e = new N({
                    width: r,
                    height: L.DIMENSION.H_TIME_PART
                }),
                n = e.g,
                i = e.canvas,
                i.style.position = "absolute",
                C.appendChild(i),
                I.appendChild(C)
            }, b = function(e) {
                var n = !1;
                if (e) {
                    E && (n = E.setTheme(e));
                    for (var a in e)
                        e.hasOwnProperty(a) && L.COLOR.hasOwnProperty(a) && L.COLOR[a] !== e[a] && (L.COLOR[a] = e[a],
                        n = !0);
                    t.stc("k_thm", e)
                }
                return n && w.styleLogo({
                    logo: s,
                    color: L.COLOR.LOGO
                }),
                n
            }, y = function(e) {
                !L.custom.mousewheel_zoom || document.activeElement !== C && document.activeElement.parentNode !== C || (A && A.onWheel(e),
                u.preventDefault(e),
                u.stopPropagation(e))
            }, k = function(e) {
                L.custom.keyboard && A && A.onKb(e)
            }, S = function() {
                t.xh5_deviceUtil.istd || (g.info.name.match(/firefox/i) ? u.addHandler(C, "DOMMouseScroll", y) : u.addHandler(C, "mousewheel", y),
                C.tabIndex = 0,
                u.addHandler(C, "keyup", k),
                u.addHandler(C, "keydown", k))
            }, M = function(e) {
                s = e,
                C.appendChild(e)
            };
            v(),
            p(),
            b(a.theme),
            f(),
            S(),
            w.getLogo({
                cb: M,
                id: L.PARAM.LOGO_ID,
                isShare: !1,
                top: L.DIMENSION.posY + L.DIMENSION.H_MA4K + 17,
                right: L.DIMENSION.RIGHT_W + L.DIMENSION.K_RIGHT_W,
                LOGO_W: L.DIMENSION.LOGO_W,
                LOGO_H: L.DIMENSION.LOGO_H,
                color: L.COLOR.LOGO
            }),
            g.noH5 && (Y.showTip({
                txt: a.nohtml5info || _.nohtml5info,
                parent: C
            }),
            t.stc("k_nh5")),
            this.resizeAll = f,
            this.innerResize = function(e) {
                A && (h(0 / 0, 0 / 0, e),
                A.onResize(),
                B.onResize(),
                m(),
                z.onInnerResize({
                    height: L.DIMENSION.h_k
                }))
            }
            ,
            this.initTheme = b,
            this.drawReMark = function(t) {
                if (t) {
                    if (i.style.display = "",
                    o == t)
                        return;
                    var a = L.DIMENSION.H_TIME_PART;
                    o = t,
                    e.resize({
                        width: r,
                        height: a,
                        hd: L.PARAM.getHd()
                    }),
                    n.font = "12px " + L.STYLE.FONT_FAMILY,
                    n.textBaseline = "top",
                    n.fillStyle = L.COLOR.REMARK_BG,
                    n.fillRect(0, 0, r, a),
                    n.fillStyle = L.COLOR.REMARK_T,
                    n.fillText(t, 0, 0)
                } else
                    i.style.display = "none"
            }
        }
        , B = new function() {
            var e, n, i, o, s = t.market(a.symbol), r = /^forex|^HF/.test(s), d = isNaN(a.nfloat) ? 2 : a.nfloat, u = 150, p = new function() {
                var t = function(t) {
                    var n = e.body.style;
                    t && L.custom.show_floater ? (n.backgroundColor = L.COLOR.F_BG,
                    n.color = L.COLOR.F_T,
                    n.border = "1px solid " + L.COLOR.F_BR,
                    n.display = "") : n.display = "none"
                };
                this.pv = function(n) {
                    var a = e.body.style
                      , i = Math.max(L.DIMENSION.posX, 55) + 9;
                    a.left = (n.x > L.DIMENSION.getStageW() >> 1 ? i : L.DIMENSION.getStageW() - u - 9) + "px",
                    a.top = (n.y || 0) + "px",
                    t(!0)
                }
                ,
                this.showFloater = t
            }
            , f = function() {
                function a() {
                    var e, n, a = "border:0;font-size:100%;font:inherit;vertical-align:baseline;margin:0;padding:0;border-collapse:collapse;border-spacing:0;text-align:center;", i = "font-weight:normal;border:0;height:16px;text-align:center", o = "text-align:left;font-weight:normal;border:0;height:16px;padding:0", s = "text-align:right;border:0;height:16px;padding:0", h = c("div"), p = h.style;
                    p.position = "absolute",
                    p.zIndex = L.PARAM.I_Z_INDEX + 2,
                    p.padding = "2px",
                    p.width = u + "px",
                    p.lineHeight = "16px",
                    p.display = "none",
                    p.fontSize = "12px";
                    var f, v, g, b, N = c("table"), _ = c("thead"), w = c("tbody");
                    N.style.cssText = a,
                    f = c("tr"),
                    v = c("th"),
                    v.setAttribute("colspan", "2"),
                    v.style.cssText = i;
                    var k = c("span");
                    v.appendChild(k),
                    f.appendChild(v),
                    _.appendChild(f),
                    f = c("tr"),
                    v = c("th"),
                    v.setAttribute("colspan", "2"),
                    v.style.cssText = i;
                    var S = c("span");
                    v.appendChild(S),
                    f.appendChild(v),
                    w.appendChild(f),
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u5f00\u76d8";
                    var M = c("span");
                    g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(M),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u6700\u9ad8";
                    var A = c("span");
                    g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(A),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u6700\u4f4e";
                    var I = c("span");
                    g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(I),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u6536\u76d8";
                    var C = c("span");
                    g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(C),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u6da8\u8dcc";
                    var x = c("span");
                    if (g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(x),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    !r) {
                        f = c("tr"),
                        v = c("th"),
                        v.style.cssText = o,
                        g = c("td"),
                        b = c("span"),
                        b.innerHTML = "\u6210\u4ea4";
                        var R = c("span");
                        g.style.cssText = s,
                        v.appendChild(b),
                        g.appendChild(R),
                        f.appendChild(v),
                        f.appendChild(g),
                        w.appendChild(f),
                        f = c("tr"),
                        v = c("th"),
                        v.style.cssText = o,
                        g = c("td"),
                        b = c("span"),
                        b.innerHTML = "\u6362\u624b";
                        var D = c("span");
                        g.style.cssText = s,
                        v.appendChild(b),
                        g.appendChild(D),
                        f.appendChild(v),
                        f.appendChild(g),
                        w.appendChild(f),
                        D.innerHTML = "--"
                    }
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u632f\u5e45";
                    var H = c("span");
                    g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(H),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u76d8\u540e\u91cf";
                    var O = c("span");
                    g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(O),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    f.id = "__floatingPostVolume",
                    f.style.display = "none",
                    f = c("tr"),
                    v = c("th"),
                    v.style.cssText = o,
                    g = c("td"),
                    b = c("span"),
                    b.innerHTML = "\u76d8\u540e\u989d";
                    var K = c("span");
                    g.style.cssText = s,
                    v.appendChild(b),
                    g.appendChild(K),
                    f.appendChild(v),
                    f.appendChild(g),
                    w.appendChild(f),
                    f.id = "__floatingPostAmount",
                    f.style.display = "none",
                    O.innerHTML = K.innerHTML = "--",
                    N.appendChild(_),
                    N.appendChild(w),
                    N.style.width = "100%",
                    h.appendChild(N);
                    var T, U, E = function(e, t) {
                        var n = L.COLOR.F_N;
                        return e > t ? n = L.COLOR.F_RISE : t > e && (n = L.COLOR.F_FALL),
                        n
                    }, P = function(e, t) {
                        return t ? "(" + ((e - t) / Math.abs(t) * 100).toFixed(2) + "%)" : "(--%)"
                    };
                    this.setFloaterData = function(a) {
                        if (e = a.name || a.symbol || e || "",
                        k.innerHTML = e,
                        T = a.data || n) {
                            n = T,
                            U = a.stock || U;
                            var i = U.market
                              , o = "";
                            switch (i) {
                            case "CN":
                            case "OTC":
                            case "REPO":
                                o = "G" == U.hq.KCBType || "GC" == U.hq.KCBType ? "" : "\u624b";
                                break;
                            case "US":
                            case "HK":
                                o = "\u80a1";
                                break;
                            default:
                                o = ""
                            }
                            var s = T.percent
                              , c = T.open
                              , h = T.close
                              , u = T.high
                              , p = T.low
                              , f = h / (1 + s) || T.prevclose;
                            S.innerHTML = m.ds(T.date, "/") + "/" + m.nw(T.date.getDay()) + (T.time || "");
                            var v = 1 > f || 1 > u || 1 > p ? 4 : d;
                            M.innerHTML = c.toFixed(v) + P(c, f, v),
                            A.innerHTML = u.toFixed(v) + P(u, f, v),
                            I.innerHTML = p.toFixed(v) + P(p, f, v),
                            C.innerHTML = h.toFixed(v) + P(h, f, v),
                            s = isNaN(s) || !isFinite(s) ? "--" : (100 * s).toFixed(2),
                            x.innerHTML = T.change.toFixed(v) + "(" + s + "%)";
                            var g = isNaN(T.ampP) ? "--" : (100 * T.ampP).toFixed(2);
                            if (T.ampP === 1 / 0 && (g = "--"),
                            H.innerHTML = T.amplitude.toFixed(v) + "(" + g + "%)",
                            x.style.color = E(s, 0),
                            M.style.color = E(c, f),
                            A.style.color = E(u, f),
                            I.style.color = E(p, f),
                            C.style.color = E(h, f),
                            r || (R.innerHTML = y(T.volume, 2) + o),
                            D && U) {
                                var b = U.extraDataObj.rsAmount;
                                if (b) {
                                    for (var N, _ = 0, w = b.length; w > _; _++)
                                        if (T.date >= b[_].date) {
                                            N = b[_].amount;
                                            break
                                        }
                                    U.hq && U.hq.isKCB && N,
                                    N && (D.innerHTML = (T.volume / N).toFixed(2) + "%")
                                } else
                                    D.innerHTML = "--"
                            }
                            24 === V.viewId || 23 === V.viewId || 25 === V.viewId ? U.hq && (U.hq.isKCB || U.hq.isCYB) && (l("__floatingPostVolume").style.display = "table-row",
                            l("__floatingPostAmount").style.display = "table-row",
                            T.postVol ? (O.innerHTML = t.strUtil.vs(T.postVol, !0) + o,
                            K.innerHTML = t.strUtil.vs(T.postAmt, !0)) : (K.innerHTML = "--",
                            O.innerHTML = "--")) : (l("__floatingPostVolume").style.display = "none",
                            l("__floatingPostAmount").style.display = "none")
                        }
                    }
                    ,
                    this.body = h,
                    this.reset = function() {
                        e = null,
                        n = null
                    }
                }
                n = new a,
                e = n
            }, v = function() {
                function e(e) {
                    var t = c("div")
                      , n = c("div")
                      , a = c("span")
                      , i = 12
                      , o = e.isH
                      , s = function() {
                        if (n.style.borderStyle = "dashed",
                        n.style.borderColor = L.COLOR.IVH_LINE,
                        a.style.backgroundColor = L.COLOR[e.txtBgCN],
                        a.style.color = L.COLOR[e.txtCN],
                        o)
                            n.style.borderWidth = "1px 0 0 0",
                            t.style.width = n.style.width = L.DIMENSION.getStageW() + "px",
                            a.style.top = -(.6 * L.STYLE.FONT_SIZE) + "px",
                            a.style.width = L.DIMENSION.extend_draw ? "" : L.DIMENSION.posX + "px",
                            a.style.left = 0,
                            a.style.padding = "1px 0";
                        else {
                            n.style.borderWidth = "0 1px 0 0";
                            var i, s, r = L.DIMENSION.H_MA4K + L.DIMENSION.H_T_B;
                            L.DIMENSION.getStageH() < 0 ? (i = H.clientHeight,
                            s = i - r) : (i = L.DIMENSION.getStageH() - O.clientHeight || 0,
                            s = L.DIMENSION.h_k),
                            i -= r,
                            i += L.DIMENSION.I_V_O,
                            t.style.height = n.style.height = i + "px",
                            a.style.top = s + "px",
                            a.style.padding = "2px 2px 1px"
                        }
                    };
                    t.style.position = "absolute",
                    t.style.zIndex = L.PARAM.I_Z_INDEX - 2,
                    a.style.position = n.style.position = "absolute",
                    n.style.zIndex = 0,
                    a.style.zIndex = 1,
                    a.style.font = L.STYLE.FONT_SIZE + "px " + L.STYLE.FONT_FAMILY,
                    a.style.whiteSpace = "nowrap",
                    a.style.lineHeight = i + "px",
                    e.txtA && (a.style.textAlign = e.txtA),
                    s(),
                    t.appendChild(a),
                    t.appendChild(n);
                    var r = function(e) {
                        e ? "" != t.style.display && (t.style.display = "") : "none" != t.style.display && (t.style.display = "none")
                    };
                    this.pv = function(e) {
                        if (!isNaN(e.y) && (t.style.top = e.y + (e.oy || 0) + "px"),
                        a.innerHTML = e.v || "",
                        !isNaN(e.x)) {
                            e.x < 0 && (e.x = 0);
                            var n = e.x + (e.ox || 0)
                              , i = L.DIMENSION.getStageW();
                            n = ~~(n + .5),
                            n -= 1,
                            t.style.left = n + "px";
                            var o = a.offsetWidth || 66
                              , s = o >> 1;
                            e.x < s ? s = e.x : n + s > i && (s = n + o - i),
                            a.style.left = -s + "px"
                        }
                        r(!0)
                    }
                    ,
                    this.display = r,
                    this.body = t,
                    this.resize = s,
                    r(!1)
                }
                i = new e({
                    isH: !0,
                    txtCN: "P_TC",
                    txtBgCN: "P_BG",
                    txtA: "right"
                }),
                o = new e({
                    isH: !1,
                    txtCN: "T_TC",
                    txtBgCN: "T_BG",
                    txtA: "center"
                }),
                C.appendChild(o.body)
            }, g = function() {
                i.display(!1),
                o.display(!1),
                p.showFloater(!1)
            }, b = function(e) {
                T && T.indirectI(e),
                U && U.indirectI(e)
            }, N = !1, w = !1, k = 0 / 0, S = !1;
            this.getInteractiveIdx = function() {
                return k
            }
            ,
            this.isIng = function() {
                return N
            }
            ,
            this.isMoving = function() {
                return S
            }
            ;
            var I = 0 / 0
              , R = 0 / 0
              , D = [];
            this.iToD = function(t, n, a) {
                if (!t.e || !w) {
                    var s = t.x
                      , r = t.ox || 0
                      , l = t.y
                      , c = t.oy || 0
                      , h = t.e ? t.e.target : null;
                    if (!a) {
                        if (I == s && R == l)
                            return;
                        I = s,
                        R = l
                    }
                    if (h) {
                        var u = h.style.height.split("px")[0];
                        (0 > l || l > u) && (s = 0 / 0,
                        l = 0 / 0)
                    }
                    var m = V.currentLength
                      , f = Math.max(m, L.PARAM.minCandleNum);
                    s += L.DIMENSION.w_k / f - q.x;
                    var v = Math.floor(s * f / L.DIMENSION.w_k);
                    if (0 > v ? v = 0 : v >= m && (v = m - 1),
                    !isNaN(v) && (k = v),
                    isNaN(s) && isNaN(l))
                        return N = !1,
                        g(),
                        b(Number.MAX_VALUE),
                        void z.onViewPrice();
                    N = V.end != V.dataLength ? !0 : m - 1 > v;
                    for (var y, S, C, x, H, O, K, T = Number(t.mark); D.length; )
                        D.length--;
                    if (n) {
                        var U = A.getAllStock()
                          , E = U.length
                          , P = E > 1 || "percent" == L.datas.scaleType;
                        L.custom.k_overlay && (P = !1);
                        for (var F, $, Y, j, B = Number.MAX_VALUE, G = 0; E > G; G++)
                            Y = U[G],
                            H = Y.datas,
                            !H || H.length <= v || (F = Y.getName(),
                            $ = H[v],
                            D.push({
                                name: F,
                                data: $,
                                rangedata: H,
                                symbol: Y.symbol,
                                color: Y.getLineStyle().linecolor
                            }),
                            $.isFake || (j = Math.abs($.cy - l),
                            B > j && (B = j,
                            x = Y,
                            C = $,
                            K = H,
                            S = F,
                            y = x.symbol)));
                        if (P)
                            O = 100 * T,
                            O = Math.abs(O) > 999 ? Math.floor(O) : O.toFixed(2),
                            O += "%";
                        else if (O = T > 99999 ? Math.floor(T) : T.toFixed(T > 9999 ? 1 : d),
                        L.custom.show_k_rangepercent && x) {
                            var W = (T - x.prevclose) / x.prevclose * 100;
                            W = isNaN(W) || !isFinite(W) ? "--" : W.toFixed(d),
                            O += "<br/>" + W + "%"
                        }
                    } else {
                        if (x = A.getMainStock(),
                        H = x.datas,
                        !H || H.length <= v)
                            return;
                        C = H[v],
                        K = H,
                        S = x.getName(),
                        y = x.symbol;
                        var X = Math.abs(T);
                        O = X > 99999 ? Math.floor(T) : T.toFixed(X > 9999 ? 1 : d),
                        D.push({
                            name: S,
                            data: C,
                            rangedata: K,
                            symbol: y,
                            color: x.getLineStyle().linecolor
                        })
                    }
                    if (C) {
                        var Z = s;
                        L.custom.stick && (s = C.ix || s),
                        e && (e.setFloaterData({
                            symbol: y,
                            name: S,
                            data: C,
                            stock: x,
                            arr: D
                        }),
                        p.pv({
                            x: Z,
                            y: L.DIMENSION.K_F_T
                        })),
                        i.pv({
                            y: l,
                            v: O,
                            oy: c
                        }),
                        o.pv({
                            x: s,
                            ox: r,
                            y: L.DIMENSION.H_MA4K,
                            v: C.day + " " + (C.time || "")
                        }),
                        b(v),
                        !S && (S = y || "--"),
                        z.onViewPrice(C, v, D, K, S, !0),
                        M.re(_.e.I_EVT, t.e)
                    }
                }
            }
            ;
            var K, E, P;
            this.iToKb = function(e, t) {
                if (t)
                    return void (w = !1);
                if (w = !0,
                k += e,
                !h(x, B.iHLineO.body) && x.appendChild(B.iHLineO.body),
                K = A.getMainStock(),
                P = K.getName(),
                E = K.datas,
                !E)
                    return void 0;
                if (0 > k)
                    return k = 0,
                    -1;
                if (k >= E.length)
                    return k = E.length - 1,
                    1;
                var n = E[k];
                if (!n)
                    return void 0;
                var a = {
                    mark: K.labelMaxP - n.cy / L.DIMENSION.h_k * (K.labelMaxP - K.labelMinP),
                    x: n.ix,
                    y: n.cy,
                    oy: L.DIMENSION.H_MA4K,
                    ox: L.DIMENSION.posX
                };
                return void this.iToD(a, !0, !0)
            }
            ;
            var F;
            this.globalDragHandler = function(e, t, n, a, i) {
                if (isNaN(e) && isNaN(t))
                    return F = 0 / 0,
                    S = !1,
                    void M.re(_.e.I_EVT, i);
                g();
                var o = V.start
                  , s = V.end
                  , r = s - o;
                isNaN(F) && (F = e);
                var l = t - F
                  , c = V.dataLength
                  , h = L.DIMENSION.w_k / r;
                if (Math.abs(l) < h) {
                    if (L.custom.smooth && h > 4) {
                        if (s >= c && 0 > l)
                            return;
                        if (1 > o && l > 0)
                            return;
                        q.x = l,
                        A.callSdDraw()
                    }
                } else {
                    F = t;
                    var d = Math.round(l * r / L.DIMENSION.w_k);
                    o -= d,
                    s -= d,
                    s >= c && (s = c,
                    o = s - r),
                    0 > o && (o = 0,
                    s = r),
                    (V.start != o || V.end != s) && (q.resetX(0),
                    V.movY = a - n,
                    A.moving(o, s, !0),
                    S = !0)
                }
            }
            ,
            this.shortClickHandler = function() {
                z.shortClickHandler()
            }
            ,
            this.zoomView = function(e, t) {
                var n = -Number(e);
                0 == n && (n = 1);
                var a = V.start
                  , i = V.end
                  , o = n * Math.ceil((i - a) / L.PARAM.zoomUnit);
                if (Math.abs(o) > L.PARAM.zoomLimit && (o = n * L.PARAM.zoomLimit),
                L.custom.centerZoom) {
                    var s = Math.min.apply(Math, t)
                      , r = s / L.DIMENSION.w_k
                      , l = Math.max.apply(Math, t)
                      , c = l / L.DIMENSION.w_k;
                    r < L.PARAM.zoomArea ? i = Math.min(i - o * Math.abs(o), V.dataLength) : c > 1 - L.PARAM.zoomArea ? a = Math.max(a + o * Math.abs(o), 0) : (a = Math.max(a + o * Math.abs(o), 0),
                    i = Math.min(i - o * Math.abs(o), V.dataLength))
                } else
                    a = Math.max(a + o * Math.abs(o), 0);
                A.moving(a, i)
            }
            ,
            f(),
            v(),
            this.onResize = function() {
                i.resize(),
                o.resize()
            }
            ,
            this.iHLineO = i,
            this.hideIUis = g,
            this.update = function() {
                N || (b(Number.MAX_VALUE),
                e && e.setFloaterData({}))
            }
            ,
            this.iReset = function() {
                e.reset && e.reset()
            }
            ,
            this.patcher = new function() {
                var a, i = {}, o = function() {
                    if (a) {
                        e.body.parentNode && e.body.parentNode.removeChild(e.body);
                        var t = "vid_" + V.viewId;
                        if (a[t]) {
                            var o;
                            o = i[t] ? i[t] : i[t] = new a[t],
                            e = o
                        } else
                            e = n
                    } else
                        e = n;
                    !h(C, e.body) && C.appendChild(e.body)
                };
                this.customFloater = function(e) {
                    a = e,
                    o(),
                    t.stc("k_fl", e)
                }
                ,
                this.switchFloater = o
            }
        }
        ;
        A = new S;
        var G = new function() {
            var e = this;
            this.resize = function(e, t) {
                j.resizeAll(!0, e, t)
            }
            ;
            var n, a = function(n, a) {
                if (L.hasOwnProperty(n)) {
                    for (var i in a)
                        if (a.hasOwnProperty(i) && t.isFunc(a[i]))
                            return;
                    "DIMENSION" == n && ($ = 1),
                    p(L[n], a),
                    t.stc(n, a),
                    e.resize()
                }
            }, i = function(e, n) {
                var a;
                if (L.hasOwnProperty(e)) {
                    a = t.clone(L[e], null);
                    for (var i in a)
                        if (a.hasOwnProperty(i))
                            if (t.isFunc(a[i]))
                                a[i] = null,
                                delete a[i];
                            else if (n)
                                for (var o = n.length; o--; )
                                    typeof a[i] === n[o] && (a[i] = null,
                                    delete a[i])
                }
                return a
            }, o = function(e, t, n) {
                n = p({
                    toremove: !1,
                    isexclusive: !1,
                    callback: void 0,
                    addon: !1
                }, n || {}),
                n.toremove ? A.mM.removeAC(t, e) : n.isexclusive ? (A.mM.removeAC(null, e),
                A.mM.newAC(t, e, n)) : A.mM.newAC(t, e, n)
            };
            this.setLineStyle = function(e, a) {
                a || (n = e),
                A.setLineStyle(e),
                t.stc("k_style", e)
            }
            ,
            this.showScale = function(e) {
                A.setScale(e),
                t.stc("k_scale", e)
            }
            ,
            this.pushData = function(e, n) {
                !t.isArr(e) && (e = [e]),
                A.pushData(e, n)
            }
            ;
            var s, r, c = [], h = function() {
                if (c.length) {
                    var e = c.shift();
                    A.pushData([e], 1)
                } else
                    clearInterval(r)
            }, d = function() {
                r = setInterval(h, 1)
            };
            this.pushTr = function(e) {
                if (e && e.data) {
                    for (var t, n = e.data.split(","), a = e.symbol, i = e.market, o = 0, r = n.length; r > o; o++)
                        t = {
                            symbol: a,
                            data: n[o],
                            market: i
                        },
                        c.push(t);
                    clearTimeout(s),
                    s = setTimeout(d, 20)
                }
            }
            ,
            this.hide = function(e) {
                F = !0,
                B.hideIUis(),
                t.$CONTAINS(I, C) && I.removeChild(C),
                e && A.dcReset()
            }
            ,
            this.show = function(e) {
                F = !1,
                e && (t.isStr(e) && (e = l(e)),
                I = e),
                t.$CONTAINS(I, C) || (I.appendChild(C),
                j.resizeAll(!0)),
                A.outputNewRange(!0),
                z.onViewPrice()
            }
            ;
            var u = 0
              , m = !1
              , f = function(e) {
                var t;
                switch (e) {
                case 1:
                    t = "\u540e\u590d\u6743";
                    break;
                case -1:
                    t = "\u524d\u590d\u6743"
                }
                j.drawReMark(t)
            }
              , v = []
              , g = []
              , y = function() {
                for (; v.length; ) {
                    var e = v.pop();
                    g.length--,
                    A.compare(e)
                }
            }
              , N = function() {
                for (var e, t = A.getMainStock().symbol, n = A.getMainStock().market, a = A.getAllStock(), i = a.length; i--; ) {
                    e = a[i];
                    var o = e.symbol;
                    if (o != t) {
                        var s = e.market;
                        s != n && ("US" == s || "US" == n || "HK" == s || "HK" == n || "OTC" == s || "OTC" == n || "option_cn" == s || "option_cn" == n) && (v.push(e),
                        g.push(o))
                    }
                }
                g.length && A.removeCompare(g, !0)
            }
              , w = function() {
                m = !1,
                e.setLineStyle(void 0, !0),
                e.showScale(void 0),
                A.mM.togglePt({
                    v: !0,
                    ytd: !0
                })
            }
              , k = function(e) {
                "mink" == _.URLHASH.gt(e).type ? (V.viewId = e,
                f(),
                N()) : (e += u,
                V.viewId = e,
                f(u),
                y())
            }
              , S = new function() {
                this.isClMode = !1,
                this.exitClMode = function() {
                    this.isClMode = !1,
                    e.setLineStyle(n, !0),
                    A.mM.togglePt({
                        v: !0,
                        ytd: !0
                    })
                }
                ,
                this.enterClMode = function() {
                    this.isClMode = !0;
                    var t = n && "mountain" == n.linetype ? "mountain" : "line";
                    e.setLineStyle({
                        linetype: t,
                        linecolor: {
                            K_CL: L.COLOR.T_P
                        }
                    }, !0),
                    A.mM.togglePt({
                        v: !1,
                        ytd: !0
                    })
                }
            }
              , x = !0;
            this.showView = function(e, n, a) {
                B.hideIUis(),
                x ? setTimeout(function() {
                    x = !1
                }, 99) : P.hide();
                var i = t.isNum(e) ? _.URLHASH.vn(e) : _.URLHASH.vi(e);
                if (i) {
                    if (m && w(),
                    i == _.URLHASH.KCL)
                        S.enterClMode();
                    else {
                        S.isClMode && S.exitClMode();
                        var o = A.getAllStock()
                          , s = o && o.length > 1;
                        s && A.mM.togglePt({
                            v: !1
                        })
                    }
                    k(i),
                    A.onChangeView(!1, n),
                    t.stc("k_v", e),
                    !a && t.suda("vw", e)
                }
            }
            ;
            var R = !1;
            this.showYTD = function(e, n) {
                R = !!e,
                B.hideIUis(),
                m || (m = !0,
                this.setLineStyle({
                    linetype: "line",
                    linecolor: {
                        K_CL: L.COLOR.T_P
                    }
                }, !0),
                !R && this.showScale("percent"),
                A.mM.togglePt({
                    v: !1,
                    ytd: !0
                })),
                f(u),
                A.showYTD(u, R),
                t.stc("k_v", _.URLHASH.NYTD),
                !n && t.suda("vw", _.URLHASH.NYTD)
            }
            ,
            this.showYear = function() {
                this.showYTD(!0)
            }
            ,
            this.setReK = function(e) {
                if (e = parseInt(e),
                !(isNaN(e) || Math.abs(e) > 1)) {
                    u = e;
                    var n = _.URLHASH.gt(V.viewId);
                    t.stc("k_re", e);
                    var a = e;
                    "-1" == a && (a = "_1"),
                    t.suda("k_re", "k_re" + a),
                    "mink" != n.type && (m ? this.showYTD(R, !0) : this.showView(n.baseid, void 0, !0))
                }
            }
            ;
            var D = function(e) {
                var n;
                return n = t.isStr(e) ? e.split(",") : [e.symbol]
            };
            this.compare = function(e, n) {
                if (n) {
                    for (var a = D(e), i = a.length; i--; )
                        for (var o = g.length; o--; )
                            if (a[i] == g[o]) {
                                g.splice(o, 1),
                                v.splice(o, 1);
                                break
                            }
                    A.removeCompare(D(e))
                } else
                    A.compare(e),
                    t.suda("k_comp");
                t.stc("k_comp", {
                    rm: n,
                    o: e
                })
            }
            ;
            var H = 0;
            this.tCharts = function(e, n) {
                o("tech", e, n),
                n && !n.noLog && (0 == H ? H = 1 : t.sudaLog())
            }
            ;
            var O = 0;
            this.pCharts = function(e, n) {
                o("price", e, n),
                n && !n.noLog && (0 == O ? O = 1 : t.sudaLog())
            }
            ,
            this.showPCharts = function(e) {
                e && (A.mM.togglePt(e),
                t.stc("k_sp", e))
            }
            ,
            this.getIndicators = function() {
                var e = T ? T.getLog() : null
                  , t = U ? U.getLog() : null;
                return {
                    tCharts: e,
                    pCharts: t
                }
            }
            ,
            this.getIndicatorData = function() {
                var e = T ? T.getExistingCharts() : null
                  , t = U ? U.getExistingCharts() : null;
                return {
                    tCharts: e,
                    pCharts: t
                }
            }
            ;
            var q;
            this.showRangeSelector = function(e) {
                q = p({
                    display: !0,
                    from: void 0,
                    to: void 0
                }, e || {}),
                A.mM.showRs(q),
                t.stc("k_rs", e)
            }
            ,
            this.dateFromTo = function(e, n, a) {
                E && (E.dateFromTo(e, n, a),
                t.stc("k_ft", [e, n, a]))
            }
            ,
            this.setCustom = b(a, this, "custom"),
            this.setTheme = function(e) {
                var t = j.initTheme(e);
                t && (this.setLineStyle({
                    linecolor: e
                }),
                this.resize())
            }
            ,
            this.setDimension = b(a, this, "DIMENSION"),
            this.getDimension = b(i, null, "DIMENSION", ["boolean"]),
            this.newSymbol = function(e) {
                if (B.hideIUis(),
                B.iReset(),
                A.dcReset(),
                A.dcInit(e),
                Y.hideTip(),
                T) {
                    var n = T.getLog();
                    T = null,
                    n && this.tCharts(n)
                }
                if (U) {
                    var a = U.getLog();
                    U = null,
                    a && this.pCharts(a)
                }
                q && (q.from = void 0,
                q.to = void 0,
                A.mM.showRs(q)),
                A.h5tM.resetHisT(),
                t.stc("k_ns", e)
            }
            ,
            this.toggleExtend = function() {
                var e = L.DIMENSION.extend_draw
                  , t = L.DIMENSION.posX;
                a.call(this, "DIMENSION", {
                    extend_draw: !e,
                    posX: t > 9 ? 7 : 55
                }),
                this.resize()
            }
            ,
            this.shareTo = function(e) {
                A.shareTo(e),
                t.stc("k_share", e);
                var n = e && e.type ? e.type : "weibo";
                t.suda("share", n)
            }
            ,
            this.getChartId = function() {
                return L.uid
            }
            ,
            this.getSymbols = function() {
                return A.getAllSymbols()
            }
            ,
            this.patcher = {
                iMgr: B.patcher
            },
            this.getExtraData = function(e) {
                return A.getExtraData(e)
            }
            ,
            this.getCurrentData = function() {
                var e = K.get(V.viewId);
                return e && (e = e[e.length - 1]),
                t.clone(e, null)
            }
            ,
            this.getCurrentRange = function() {
                for (var e, t, n, a = [], i = A.getAllStock(), o = 0, s = i.length; s > o; o++)
                    n = i[o],
                    t = n.getName(),
                    e = n.datas,
                    a.push({
                        name: t,
                        rangedata: e,
                        symbol: n.symbol
                    });
                return a
            }
            ,
            this.zoom = function(e) {
                A.zoomApi(e),
                t.stc("k_zoom", e, 9e3)
            }
            ,
            this.rangeMove = function(e, t) {
                A.moving(e, t)
            }
            ,
            this.move = function(e) {
                e = parseInt(e),
                isNaN(e) || (A.moveApi(e),
                t.stc("k_move", e, 9e3))
            }
            ,
            this.update = function() {
                A.updateDataAll(),
                t.stc("k_up", 9e3)
            }
            ,
            this.type = "h5k",
            this.me = M
        }
        ;
        return A.dcInit(a),
        G
    }
    function i() {
        this.get = function(e, n) {
            t.stc("h5k_get");
            var i = new a(e);
            t.isFunc(n) && n(i),
            t.suda("h5k_" + t.market(e.symbol))
        }
        ,
        this.dual = function(e, n) {
            t.stc("h5k_dual"),
            e.linetype = "line";
            var i = new a(e);
            i.setCustom({
                k_overlay: !0
            });
            var o = function(t) {
                i.me.rl(t, o);
                var n = e.dual;
                i.compare({
                    symbol: n.symbol,
                    name: n.name,
                    datas: n.datas,
                    linetype: "line",
                    linecolor: n.theme
                })
            };
            i.me.al(_.e.K_DATA_LOADED, o, !1),
            t.isFunc(n) && n(i),
            t.suda("dual_" + t.market(e.symbol))
        }
        ,
        this.tick = function(e, n) {
            t.stc("h5k_tick"),
            e.pcm = 1,
            e.view = _.URLHASH.NKMS,
            e.rate = 600,
            e.linetype = "line";
            var i = new a(e,!0);
            t.isFunc(n) && n(i),
            KKE.api("patch.atick.customfloater", {
                chart: i
            }, function(e) {
                i.patcher.iMgr.customFloater(e)
            }),
            i.setCustom({
                smooth: !1
            }),
            t.suda("tick_" + t.market(e.symbol))
        }
    }
    var o, s, r, l = t.$DOM, c = t.$C, h = t.$CONTAINS, d = t.xh5_PosUtil, u = t.xh5_EvtUtil, p = t.oc, m = t.dateUtil, f = m.stbd, v = t.xh5_ADJUST_HIGH_LOW.c, g = t.xh5_BrowserUtil, b = t.fBind, y = t.strUtil.ps, N = n.xh5_Canvas, _ = e.globalCfg, w = t.logoM;
    return t.fInherit(a, t.xh5_EvtDispatcher),
    i
});
;