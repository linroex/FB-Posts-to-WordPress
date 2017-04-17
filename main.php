<?php
/**
 * Plugin Name: IMPORT
 * Plugin URI: https://github.com/linroex/wordpress-post-statistics-from-google
 * Description: Import Google Analytics data in WordPress.
 * Version: 0.0.1
 * Author: linroex
 * Author URI: http://me.coder.tw
 * License: MIT
 */

function load() {
    $posts = json_decode(file_get_contents(__DIR__ . '/posts.json'));
    $image_id = 18;

    foreach ($posts as $post) {
        $post_id = wp_insert_post([
            'post_author' => 1,
            'post_date' => $post->created_time,
            'post_content' => $post->message,
            'post_title' => $post->id
        ]);

        set_post_thumbnail($post_id, $image_id);

        $image_id += 1;
    }
    
    exit();
}

add_action('activated_plugin', 'load');