from app import server

@server.route('/', methods=['GET', 'POST'])
def index():
	return 'hello world'