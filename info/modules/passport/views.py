from flask import current_app, jsonify, make_response, request
from info import constants, redis_store
from . import passport_blu
from info.utils.captcha.captcha import captcha
from info.utils.response_code import RET


@passport_blu.route('/image_code')
def get_iamge_code():
    '''
    获取图片验证码
    :return:
    '''
    # 1. 获取到当前的图片编号id   url = 127.0.0.1:5000/passport/image_code?code_id=xxxxxx
    code_id = request.args.get('code_id')
    # 2. 生成验证码
    name, text, image = captcha.generate_captcha()
    try:
        # 保存当前生成的图片验证码内容    setex(key, time, value)
        redis_store.setex('ImageCode_'+code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        return make_response(jsonify(errno=RET.DATAERR, errmsg='保存图片验证码失败'))

    # 返回响应内容
    resp = make_response(image)
    # 设置内容类型
    resp.headers['Content-Type'] = 'image/jpg'
    return resp