<?php
$link_key = MV_SLIDER_LINK_TEXT_METADATA;
$url_key = MV_SLIDER_LINK_URL_METADATA;
$link_text = get_post_meta($post->ID, $link_key, true);
$link_url = get_post_meta($post->ID, $url_key, true);
?>
 
<table class="form-table mv-slider-metabox">
	<input type="hidden" name="mv_slider_nonce" value="<?= wp_create_nonce("mv_slider_nonce")?>">
	<tr>
		<th>
			<label for="<?= esc_attr($link_key)?>"> Link Text</label>
		</th>
		<td>
			<input
				type="text"
				name="<?= esc_attr($link_key)?>"
				id="<?= esc_attr($link_key)?>"
				class="regular-text link-text"
				value="<?= esc_html($link_text)?>"
				required
			/>
		</td>
	</tr>
	<tr>
		<th>
			<label for="<?= esc_attr($url_key)?>">Link URL</label>
		</th>
		<td>
			<input
				type="url"
				name="<?= esc_attr($url_key)?>"
				id="<?= esc_attr($url_key)?>"
				class="regular-text link-text"
				value="<?= esc_url($link_url)?>"
				required
			/>
		</td>
	</tr>
</table>
