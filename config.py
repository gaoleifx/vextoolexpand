import os

class Config:
    # 基础路径配置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    VEX_PATH = os.path.join(BASE_DIR, "vex")
    PRESET_PATH = os.path.join(BASE_DIR, "preset")
    
    # 日志配置
    LOG_PATH = os.path.join(BASE_DIR, "logs")
    LOG_LEVEL = "INFO"
    
    @classmethod
    def init(cls):
        """初始化配置"""
        os.makedirs(cls.VEX_PATH, exist_ok=True)
        os.makedirs(cls.PRESET_PATH, exist_ok=True)
        os.makedirs(cls.LOG_PATH, exist_ok=True) 