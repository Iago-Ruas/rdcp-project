<?php

if (!class_exists('RDPC_Settings')) {

    class RDPC_Settings
    {
        private static $rdpc_options;
        private static $rdpc_group_settings_id;

        private $first_section_settings;
        private $first_section_field_settings;

        private $second_section_settings;
        private $second_section_field_settings;

        private $third_section_settings;
        private $third_section_field_settings;

        public function __construct()
        {
            self::$rdpc_options = get_option(RDPC_OPTIONS_SETTINGS);
            self::$rdpc_group_settings_id = RDPC_GROUP_SETTINGS_ID;

            //          ---> FIRST PAGE <---

            // First Section
            $this->first_section_settings = [
                'id' => 'first_page_main_section',
                'title' => 'Main Section',
                'callback_function' => null,
                'showing_page' => 'main_settings1',
            ];
            $this->first_section_field_settings = [
                'id' => 'first_section_item_1',
                'title' => '1-1',
                'callback_function' => [$this, 'mv_slider_shortcode_callback' ],
                'showing_page' => $this->first_section_settings['showing_page'],
                'showing_section' => $this->first_section_settings['id'],
            ];

            // Second Section
            $this->second_section_settings = [
                'id' => 'first_page_second_section',
                'title' => 'Second Section',
                'callback_function' => null,
                'showing_page' => 'main_settings2',
            ];
            $this->second_section_field_settings = [
                'id' => 'second_section_item_1',
                'title' => '2-1',
                'callback_function' => [$this, 'mv_slider_shortcode_callback' ],
                'showing_page' => $this->second_section_settings['showing_page'],
                'showing_section' => $this->second_section_settings['id'],
            ];

            // Third Section
            $this->third_section_settings = [
                'id' => 'first_page_third_section',
                'title' => 'Third Section',
                'callback_function' => null,
                'showing_page' => 'main_settings3',
            ];
            $this->third_section_field_settings = [
                'id' => 'mv_slider_shortcode',
                'title' => '3-1',
                'callback_function' => [$this, 'mv_slider_shortcode_callback' ],
                'showing_page' => $this->third_section_settings['showing_page'],
                'showing_section' => $this->third_section_settings['id'],
            ];

        }

    }
}
