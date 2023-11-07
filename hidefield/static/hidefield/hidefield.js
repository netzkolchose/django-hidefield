window.addEventListener("load", function () {
    (function($) {
        $(document).ready(function() {
            $('.hide-field').each(function (idx, el) {
                var $el = $(el);
                var $field = $el.parent();
                if ($field.hasClass('related-widget-wrapper'))
                    $field = $field.parent().parent();
                else
                    $field = $field.parent();
                if ($field.is('tr')) return;
                var $orig_label = $field.find(' > div > label');
                $field.prepend('<label class="hide-field_label '
                    + $orig_label.attr('class') + '" for="'
                    + $orig_label.attr('for') + '"><a href="javascript:void(0)">'
                    + $orig_label.text() + '</a></label>');
                $orig_label.addClass('hide-field_label_orig');
                $orig_label.html('<a href="javascript:void(0)">'+ $orig_label.text() + '</a>');
                if ($el.data('hide') && !$field.parent().hasClass('errors')) {
                    $field.children('div').hide();
                } else {
                    $field.children('.hide-field_label').hide();
                }
            });
            $('.hide-field_label').each(function (idx, el) {
                var $el = $(el);
                $el.on('click', function (ev) {
                    $(ev.currentTarget).next().show();
                    $(ev.currentTarget).hide();
                });
            });
            $('.hide-field_label_orig').each(function (idx, el) {
                var $el = $(el);
                $el.on('click', function (ev) {
                    $(ev.currentTarget).parent().prev().show();
                    $(ev.currentTarget).parent().hide();
                });
            });
        });
    })(django.jQuery);
});
