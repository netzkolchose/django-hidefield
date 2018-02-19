(function($) {
    $(document).ready(function() {
        $('.hide-field').each(function (idx, el) {
            var $el = $(el);
            var $field = $el.parent();
            if ($field.hasClass('related-widget-wrapper'))
                $field = $field.parent().parent();
            else
                $field = $field.parent();
            var $orig_label = $field.find(' > div > label');
            $field.prepend('<label class="hide-field_label '
                + $orig_label.attr('class') + '" for="'
                + $orig_label.attr('for') + '"><a href="javascript:void(0)">'
                + $orig_label.text() + '</a></label>');
            $orig_label.hide();
            if ($el.data('hide')) $field.children('div').hide();
        });
        $('.hide-field_label').each(function (idx, el) {
            var $el = $(el);
            $el.on('click', function (ev) {
                var $target = $(ev.currentTarget).next();
                if ($target.is(':visible'))
                    $target.hide();
                else
                    $target.show();
            });
        });
    });
})(django.jQuery);
