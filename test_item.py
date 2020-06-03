def test_language(app):
    app.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert app.find_element_by_class_name(
        'btn-add-to-basket'), 'Cтраница товара на сайте не содержит кнопку добавления в корзину'
