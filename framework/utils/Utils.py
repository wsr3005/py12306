from datetime import datetime

from framework.utils.log.Log import Log


def check(target, log):
    if not target:
        Log.error(log)
        return False
    return True


def date_format(date):
    return datetime.strptime(date,'%Y%m%d').strftime('%Y-%m-%d')


if __name__ == '__main__':
    print(date_format('20180102'))
