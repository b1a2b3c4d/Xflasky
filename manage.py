#coding:utf-8
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#创建应用
manager = Manager(app)
#添加命令解析功能
migrate = Migrate(app, db)
#添加数据库迁移功能


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
#此函数注册了程序、数据库实例以及模型，因此这些对象能直接导入 shell
manager.add_command("shell", Shell(make_context=make_shell_context))
#为 shell 命令注册一个 make_context 回调函数
manager.add_command('db', MigrateCommand)
#MigrateCommand 类使用 db 命令附加


@manager.command
def test():
    """Run the unit test"""
    import unitest
    tests = unitest.TestLoader().discover('test')
    unittest.TextTestRunner(Verbosity=2).run(tests)

if __name__ == '__main__':
#如果模块是被导入， __name__ 的值为模块名字
#如果模块是被直接执行， __name__ 的值为 '__main__'
    manager.run()