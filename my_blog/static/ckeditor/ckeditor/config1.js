/**
 * @license Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
    config.language = 'zh-cn';
    config.toolbar_A =
        [
            ['Source'],
            ['Cut','Copy','Paste','PasteText','PasteFromWord'],
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            '/',
            ['Styles','Format','Font','FontSize'],
            ['TextColor','BGColor'],
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
        ];
    config.toolbar = 'A';
    config.image_previewText = '';
    config.filebrowserImageUploadUrl = "../UploadweixinImgHandler.ashx";

    config.width = 700; //宽度
    config.height = 180; //高度
    config.skin='kama';

    //工具栏
    config.toolbar =
    [
        ['Source','Bold','Italic'],
       ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
        ['Smiley'],
        ['Styles','Font','FontSize'],
        ['TextColor'],
        ['Undo','Redo'],
        ['Image','Flash']

    ];

    //自定义表情的放置目录
//    config.smiley_path= "ckeditor/plugins/smiley/self/";
    //设置对话框一行显示几个表情
    config.smiley_columns = 11;
    //设置对话框表情  每一个表情的名字
    config.smiley_images = ["baozi1.gif",
    "baozi2.gif",
    "baozi3.gif",
    "baozi4.gif",
    "baozi5.gif",
    "baozi6.gif",
    "baozi7.gif",
    "baozi8.gif",
    "baozi9.gif",
    "baozi10.gif",
    "baozi11.gif",
    "baozi12.gif",
    "baozi13.gif",
    "baozi14.gif",
    "baozi15.gif",
    "baozi16.gif",
    "baozi17.gif",
    "baozi18.gif",
    "baozi19.gif",
    "baozi20.gif",
    "baozi21.gif",
    "baozi22.gif",
    "baozi23.gif",
    "baozi24.gif",
    "baozi25.gif",
    "baozi26.gif",
    "baozi27.gif",
    "baozi28.gif",
    "baozi29.gif",
    "baozi30.gif",
    "baozi31.gif",
    "baozi32.gif",
    "baozi33.gif",
    "baozi34.gif",
    "baozi35.gif",
    "baozi36.gif",
    "baozi37.gif",
    "baozi38.gif",
    "baozi39.gif",
    "baozi40.gif",
    "baozi41.gif",
    "baozi42.gif",
    "baozi43.gif",
    "baozi44.gif",
    "baozi45.gif",
    "baozi46.gif",
    "baozi47.gif",
    "baozi48.gif",
    "baozi49.gif",
    "baozi50.gif",
    "baozi51.gif",
    "baozi52.gif",
    "baozi53.gif",
    "baozi54.gif",
    "baozi55.gif",
    "baozi56.gif",
    "baozi57.gif",
    "baozi58.gif",
    "baozi59.gif",
    "baozi60.gif",
    "baozi61.gif",
    "baozi62.gif",
    "baozi63.gif",
    "baozi64.gif",
    "baozi65.gif",
    "baozi66.gif",
    "baozi67.gif",
    "baozi68.gif",
    "baozi69.gif"
];
};