<?php

/**
 * Plugin Name: RDPC
 * Plugin URI:
 * Description: test
 * Version: 1.0
 * Requires as least:
 * Author: Iago Ruas
 * Author URI:
 * License: GPL v2 or later
 * License URI: https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain: rdpc
 * Domain Path: /languages
 */

/*
RDPC is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
any later version.

RDPC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with RDPC. If not, see https://www.gnu.org/licenses/gpl-2.0.html.
*/

if (!defined('ABSPATH')) {
    exit;
}

if (!class_exists('RDPC')) {
    class RDPC
    {
        public function __construct()
        {
            $this->define_constants();

            require_once(RDPC_PATH . 'post-types\class.rdpc-cpt.php');
            $RDPC_Post_Type = new RDPC_Post_Type();
        }

        public function define_constants()
        {
            define('RDPC_PATH', plugin_dir_path(__FILE__));
            define('RDPC_URL', plugin_dir_url(__FILE__));
            define('RDPC_Version', '1.0.0');
            define('RDPC_LINK_TEXT_METADATA', 'rdpc_link_text');
            define('RDPC_LINK_URL_METADATA', 'rdpc_link_url');
        }

        public static function activate()
        {
            update_option('rewrite_rules', '');
        }

        public static function deactivate()
        {
            flush_rewrite_rules();
            unregister_post_type('rdpc');
        }

        public static function uninstall()
        {
        }
    }
}

if (class_exists('RDPC')) {
    $rdpc = new RDPC();

    register_activation_hook(__FILE__, ['RDPC', 'activate']);
    register_deactivation_hook(__FILE__, ['RDPC', 'deactivate']);
    register_uninstall_hook(__FILE__, ['RDPC', 'uninstall']);

}
