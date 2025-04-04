import uiautomator2 as u2
import time

d = u2.connect()


def start_app():
    # com.hj.hj_agent_side.MainActivity
    # //*[@content-desc="房源管理"]

    pass


# 定义操作函数
def operate_on_number_element(element):
    # 点击第一个编号下面10个像素位置
    time.sleep(5)
    print(f'点击房源')
    x, y = element.center()
    print(f'{x}, {y}')
    d.click(x, y + 90)
    time.sleep(2)
    print('点击工作台')
    # 点击工作台
    workbench = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    workbench.click()
    time.sleep(2)
    print('变更状态')
    # 点击变更状态
    change_status = d.xpath('//*[@content-desc="变更状态"]')
    change_status.click()
    time.sleep(2)
    print('暂时下架')
    # 点击暂时下架
    temporary_off_shelf = d.xpath('//*[@content-desc="暂时下架"]')
    temporary_off_shelf.click()
    time.sleep(2)

    print('输入内容')
    # 输入内容
    input_box = d.xpath('//android.widget.EditText')
    input_box.set_text("11111111112")
    time.sleep(2)

    print('点击提交')
    # 点击提交
    submit = d.xpath('//*[@content-desc="提交"]')
    submit.click()
    time.sleep(2)

    print('点击确定')
    # 点击确定
    confirm = d.xpath('//*[@content-desc="确定"]')
    confirm.click()
    time.sleep(2)

    print('点击工作台')
    # 点击工作台
    workbench.click()
    time.sleep(2)

    print('点击上架')
    # 点击上架
    on_shelf = d.xpath('//*[@content-desc="上架"]')
    on_shelf.click()
    time.sleep(2)
    print('返回上个页面')
    # 返回上个页面
    d.press("back")
    time.sleep(2)


def get_all_elements():
    # 获取编号列表
    xpath_pattern = '//*[re:match(@content-desc, "^编号.*")]'
    number_elements = d.xpath(xpath_pattern).all()
    if number_elements:
        # number_elements[0].attrib['content-desc']
        for i in range(0, 500):
            house_key = number_elements[0].attrib['content-desc']
            print(f'房源编号{house_key}，第{i+1}个')
            operate_on_number_element(number_elements[0])
            while True:
                d.swipe(0.5, 0.8, 0.5, 0.7)  # 上划操作
                number_elements = d.xpath(xpath_pattern).all()
                if number_elements[0].attrib['content-desc'] != house_key:
                    break
                if d.xpath('//*[@content-desc="没有更多了"]').exists:
                    break
    if len(number_elements) > 1:
        operate_on_number_element(number_elements[1])
    if len(number_elements) > 2:
        operate_on_number_element(number_elements[2])


def test2():
    d.swipe(0.5, 0.8, 0.5, 0.7)
    time.sleep(3)
    # 查找包含指定文本的元素
    element = d.xpath("编号：1")

    if element.exists:
        print('click')
        # 获取元素的中心坐标
        x, y = element.center()

        # 计算元素下方50像素处的坐标
        new_y = y + 90

        # 点击新坐标位置
        d.click(x, new_y)
    else:
        print("未找到包含指定文本的元素")


if __name__ == '__main__':
    get_all_elements()
    # //*[@content-desc="下拉刷新 已选 (0/63) 提交"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]
    # test2()
    # d.swipe(0.5, 0.8, 0.5, 0.7)
    pass
