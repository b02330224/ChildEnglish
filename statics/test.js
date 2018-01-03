define(function (require) {
    function a(a) {
        if (T) return T;
        var c = $(a.container);
        return v = a, v.params || (v.params = {}), (j = $("<div class='pl-container'></div>")).appendTo(c), (C = $("<div class='page pl-list-page'></div>")).appendTo(c), y = doT.template(y, null, v.def || tplDef), h = b.setup({
            container: C,
            delegate: ".pl-list-page a",
            pageClick: function () {
                g($(this).attr("data-page"))
            }
        }), $(document).on("click", ".js-pl-praise", function (e) {
            e.preventDefault();
            $(this);
            if (!OP_CONFIG.userInfo) return void require.async("login_sns", function (a) {
                a.init()
            });
            var a = $(this);
            a.hasClass("on") ? k.praiseCancel(a) : k.praiseClick(a)
        }), T = {
            load: function () {
                g()
            }
        }
    }

    function c(a) {
        return 0 != a.page_total || a.list.length ? void 0 : (j.html("<p class='pl-none'>此节暂无同学评论</p>"), !1)
    }

    function g(a, g) {
        var C;
        g && (v.params.order = g), C = $.extend({}, v.params), C.page = a || 1, C.r = Math.random(), $.ajax({
            url: "/course/getcomment",
            dataType: "json",
            data: C,
            success: function (a) {
                if (0 === a.result) {
                    if (a = a.data, $.each(a.list, function (i, a) {
                            a.description = a.description.replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, "$1<br>$2")
                        }), c(a) === !1) return;
                    j.html(y(a)), h(+a.page_current, +a.page_total)
                }
            },
            error: function () {
            }
        })
    }

    require("/static/lib/dot/1.0.0/doT.js");
    var v, h, j, C, T, y = require("/static/template/pl-list.tpl"),
        b = require("/static/component/base/util/paging.js");
    $.ajax({
        url: "/u/card", type: "get", dataType: "json", success: function (a) {
            if (0 == a.result) {
                var c = a.data;
                $("#discus-publish").find(".user-head img").attr({
                    src: c.img,
                    alt: c.nickname
                }), $("#discus-publish").find(".user-head").attr({href: "/u/" + c.uid})
            }
        }
    });
    var k = {
        praiseClick: function (a) {
            $praise = a.find("span"), $.ajax({
                url: "/course/commentsupport",
                data: {id: a.attr("data-id")},
                type: "GET",
                dataType: "json",
                success: function (c) {
                    if (0 == c.result) {
                        var $ = parseInt($praise.text());
                        $praise.text($ + 1), a.addClass("on"), a.find("i").addClass("on icon-thumb-revert"), a.attr("title", "取消赞")
                    }
                }
            })
        }, praiseCancel: function (a) {
            $praise = a.find("span"), $.ajax({
                url: "/course/commentsupport?cancel",
                data: {id: a.attr("data-id")},
                type: "POST",
                dataType: "json",
                success: function (c) {
                    if (0 == c.result) {
                        var $ = parseInt($praise.text());
                        $praise.text($ - 1), a.removeClass("on"), a.find("i").attr("class", "icon-thumb-revert"), a.attr("title", "赞")
                    }
                }
            })
        }
    };
    return a
});