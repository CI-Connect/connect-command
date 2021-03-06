
def usage():
	yield '@'

def run(opts, args, **kwargs):
	from IPython.Shell import IPShellEmbed as embed
	if htcondor:
		import classad

	schedd = htcondor.Schedd()
	r = schedd.query()

	params = {}
	for result in r:
		for k in result.keys():
			if k in params:
				params[k] += 1
			else:
				params[k] = 1

	common = []
	for k, v in params.items():
		if v == len(r):
			common.append(k)

	common.sort()

	embed()()
