/** @param {NS} ns **/
export async function main(ns) {
	ns.tail();
	ns.disableLog('sleep');
	ns.clearLog();

	//Initial list of all available programs
	const programList = ['BruteSSH.exe',  'ServerProfiler.exe', 'AutoLink.exe', 'FTPCrack.exe', 'relaySMTP.exe', 'HTTPWorm.exe', 'SQLInject.exe', 'DeepscanV1.exe', 'DeepscanV2.exe', 'Formulas.exe']

	//Create all of the programs
	for (let prog of programList) {
		if (ns.fileExists(prog)) {
			ns.print('You already have ' + prog);
			await ns.sleep(100);
			continue;
		} else {
			ns.createProgram(prog, focus = false);
			while (ns.isBusy()) {
				await ns.sleep(100);
			}
			ns.print('Finished creating ' + prog);
		}
		//secondary list of programs to repeat creation for Int farming
		const secondList = ['ServerProfiler.exe', 'AutoLink.exe', 'DeepscanV1.exe', 'DeepscanV2.exe']

		while (true) {
			//need to remove programs first, to be able to recreate them
			for (let sec of secondList) {
				if (ns.fileExists(sec)) {
					ns.rm(sec);
					ns.print('Removed ' + sec);
					await ns.sleep(100);
				} else {
					await ns.sleep(100);
				}
			}
			//now to recreate
			for (let sec of secondList) {
				ns.createProgram(sec, focus = false);
				while (ns.isBusy()) {
					await ns.sleep(100);
				}
				ns.print('Finished creating ' + sec);
			}
		}
	}
}
