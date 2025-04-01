<?php

if (!class_exists('MV_Slider_Post_Type')) {
    class MV_Slider_Post_Type
    {
        protected $link_key;
        protected $url_key;

        public function __construct()
        {
            add_action('init', [$this, 'create_post_type']);
            add_action('add_meta_boxes', [$this, 'add_meta_boxes']);
            add_action('save_post', [$this, 'save_post'], 10, 2);
            add_filter('manage_mv-slider_posts_columns', [$this, 'mv_slider_cpt_columns']);
            add_action('manage_mv-slider_posts_custom_column', [$this, 'mv_slider_custom_columns'], 10, 2);
            add_filter('manage_edit-mv-slider_sortable_columns', [$this, 'mv_slider_sortable_columns']);
            $this->link_key = MV_SLIDER_LINK_TEXT_METADATA;
            $this->url_key = MV_SLIDER_LINK_URL_METADATA;
        }

        public function mv_slider_sortable_columns($columns)
        {
            $columns[$this->link_key] = $this->link_key;
            return $columns;
        }

        public function mv_slider_custom_columns($column, $post_id)
        {
            switch ($column) {
                case $this->link_key:
                    echo esc_html(get_post_meta($post_id, $this->link_key, true));
                    break;
                case $this->url_key:
                    echo esc_url(get_post_meta($post_id, $this->url_key, true));
                    break;
            }
        }

        public function mv_slider_cpt_columns($columns)
        {
            $columns[$this->link_key] = esc_html__('Link Text', 'mv-slider');
            $columns[$this->url_key] = esc_html__('Link URL', 'mv-slider');
            return $columns;
        }
        public function create_post_type()
        {
            register_post_type(
                'mv-slider',
                ['label' => 'Slider',
                'description' => 'Sliders',
                'labels' => [
                    'name' => 'Sliders',
                    'singular_name' => 'Slider'
                ],
                'public' => true,
                'supports' => ['title', 'editor', 'thumbnail'],
                'hierarchical' => false,
                'menu_position' => 5,
                'show_ui' => true,
                'Show_in_menu' => true,
                'show_in_admin_bar' => true,
                'show_in_nav_menus' => true,
                'can_export' => true,
                'has_archive' => true,
                'exclude_from_search' => false,
                'publicly_queryable' => true,
                'show_in_rest' => true,
                'menu_icon' => 'dashicons-sort',
                // 'register_meta_box_cd'=> [$this, 'add_meta_boxes'] --- ja está no construtor
                ]
            );
        }

        public function add_meta_boxes()
        {
            add_meta_box(
                'mv_slider_meta_box',
                'Link Options',
                [$this, 'add_inner_meta_boxes'],
                'mv-slider',
                'side',
                'high'
            );
        }

        public function add_inner_meta_boxes($post)
        {
            require_once(MV_SLIDER_PATH .'views\mv-slider_metabox.php');
        }

        public function save_post($post_id)
        {
            if (isset($_POST['mv_slider_nonce'])) {
                if (!wp_verify_nonce($_POST['mv_slider_nonce'], 'mv_slider_nonce')) {
                    return;
                }
            }

            if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
                return;
            }

            if (isset($_POST['post_type']) && $_POST['post_type'] === 'mv-slider') {
                if (!current_user_can('edit_page', $post_id)
                || !current_user_can('edit_post', $post_id)) {
                    return;
                }
            }

            if (isset($_POST['action']) && $_POST['action'] == 'editpost') {
                // validar dados SEMPRE
                $old_link_text = get_post_meta($post_id, $this->link_key, true);
                $new_link_text = sanitize_text_field($_POST[$this->link_key]);
                $old_link_url = get_post_meta($post_id, $this->url_key, true);
                $new_link_url = esc_url_raw($_POST[$this->url_key]);

                if (empty($new_link_text)) {
                    update_post_meta($post_id, $this->link_key, 'Add some text');
                } else {
                    update_post_meta($post_id, $this->link_key, $new_link_text, $old_link_text);
                }

                if (empty($new_link_url)) {
                    update_post_meta($post_id, $this->url_key, '#');
                } else {
                    update_post_meta($post_id, $this->url_key, $new_link_url, $old_link_url);
                }
            }
        }
    }
}
