import model_diff as model # as для краткой записи, не обязательно
# model_div, model_mult, model_sum
import view

def button_click():
    value_a = view.get_value() # получить данные
    value_b = view.get_value()
    model.init(value_a, value_b) # инициализировать = подготовить к работе
    result = model.do_it()
    view.view_data(result, "result")