/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	// config.skin = 'kama';
	config.imageUploadUrl = 'ckeditor/uploads';  // Specify the image upload URL
	config.imageUploadMethod = 'xhr';  // Use XHR for image uploads
	config.image2_prefillDimensions = true;  // Pre-fill image dimensions when inserting
	config.image2_compressQuality = 0.8;  // Specify the image compression quality (0.0 - 1.0)

};
