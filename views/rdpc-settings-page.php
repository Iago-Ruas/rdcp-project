<div class="wrap">
    <h1><?= esc_html(get_admin_page_title())?></h1>
    <form action="options.php" method="post">
    <?php
    settings_fields(RDPC_GROUP_SETTINGS_ID);
    do_settings_sections('main_settings1');
    do_settings_sections('main_settings2');
    do_settings_sections('main_settings3');
    submit_button('Save Settings');
    ?>
    </form>
</div>