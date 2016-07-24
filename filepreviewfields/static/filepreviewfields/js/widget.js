var $ = django.jQuery;

function find(obj, selector) {
    return $($(obj).closest('.filepreviewfield').find(selector)[0]);
}

function getClearButton(obj) {
    return find(obj, ".clear");
}

function getClearCheckbox(obj) {
    return find(obj, "input[type=checkbox]");
}

function getFile(obj) {
    return find(obj, "input[type=file]");
}

function getImg(obj) {
    return find(obj, "img");
}

function getSpan(obj) {
    return find(obj, "span");
}

function getVideo(obj) {
    return find(obj, "video");
}

$(document).on("change", ".filepreviewfield input[type=file]", function(e) {
    getClearCheckbox(this).attr("checked", false);
    getClearButton(this).removeClass("hidden");
    getImg(this).remove();
    getVideo(this).remove();
    getSpan(this).text(getFile(this).val().split("\\").reverse()[0]);
});

$(document).on("click", ".filepreviewfield input.choose", function(e) {
    getFile(this).click();
});

$(document).on("click", ".filepreviewfield input.clear", function(e) {
    var span = getSpan(this);
    getFile(this).val("");
    getImg(this).remove();
    getVideo(this).remove();
    if (span.html() != "") {
        span.html("");
    }
    else {
        getClearCheckbox(this).attr("checked", true);
    }
});
