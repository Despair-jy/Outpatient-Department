  $(function() {
            if (localStorage.getItem('year')) {
                $("#year option").eq(localStorage.getItem('year')).prop('selected', true);
            }

            $("#year").on('change', function() {
                localStorage.setItem('year', $('option:selected', this).index());
            });

             if (localStorage.getItem('month')) {
                $("#month option").eq(localStorage.getItem('month')).prop('selected', true);
            }

            $("#month").on('change', function() {
                localStorage.setItem('month', $('option:selected', this).index());
            });

              if (localStorage.getItem('name1')) {
                $("#name1 option").eq(localStorage.getItem('name1')).prop('selected', true);
            }

            $("#name1").on('change', function() {
                localStorage.setItem('name1', $('option:selected', this).index());
            });
        });
