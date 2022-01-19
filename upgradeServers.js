/** @param {NS} ns **/
//Function to find out the best servers we can buy in sets of 25, or max for current BN
function findLargestAffordableServers(ns) {
	const myCash = ns.getServerMoneyAvailable("home") / ns.getPurchasedServerLimit();
	let ram = ns.getPurchasedServerMaxRam();

	while (ns.getPurchasedServerCost(ram) > myCash && ram > 1) {
		ram /= 2;
	}
	return ram;
}

export async function main(ns) {
	/*Start with checking if there are any purchased servers, 
	If none, buy the max affordable set of 25 (or whatever max for current BN is)*/
	const bestServerUpgrade = findLargestAffordableServers(ns);
	const myServers = ns.getPurchasedServers();
	if (ns.getPurchasedServers().length == 0) {
		await ns.tprint(`You can afford ${ns.getPurchasedServerLimit()} new ${ns.nFormat(bestServerUpgrade * (1e9), "0.00b")} servers`);
		await ns.sleep(3000);
		await ns.tprint(`Buying ${ns.getPurchasedServerLimit()} new ${ns.nFormat(bestServerUpgrade * (1e9), "0.00b")} servers`);
		await ns.sleep(3000);

		//If servers are found, calculate the highest ram we can afford to upgrade to
		var i = 0;
		let needRam = ns.getScriptRam("expFarm.ns");
		const MIN_THREADS = 1;
		let threads = Math.max(MIN_THREADS, Math.floor(bestServerUpgrade / needRam));

		while (i < ns.getPurchasedServerLimit()) {
			if (ns.getServerMoneyAvailable("home") > ns.getPurchasedServerCost(bestServerUpgrade)) {
				var hostname = ns.purchaseServer("daemon-" + i, bestServerUpgrade);
				//await ns.scp("Remote/grow-target.js", hostname);
				//await ns.sleep(100)
				//await ns.scp("Remote/hack-target.js", hostname);
				//await ns.sleep(100);
				//await ns.scp("Remote/weaken-target.js", hostname);
				//await ns.sleep(100);
				//await ns.scp("helper.js", hostname);
				//await ns.exec("expFarm.ns", hostname, threads);
			}
			++i
		}
		await ns.tprint(`Scripts sent to all ${ns.getPurchasedServerLimit()} new ${hostname}-${ns.nFormat(bestServerUpgrade * (1e9), "0.00b")} servers`);
		await ns.sleep(3000);
		await ns.tprint(`Script complete`);
		await ns.sleep(100);
		await ns.exit();
	} else {
		const currentServerRam = ns.getServerMaxRam(myServers[0]);

		/*Compare best affordable upgrade to what we currently own
		Exit script if we own better
		Kill any running scripts and delete all old servers if we can upgrade*/
		for (var i = 0; i < myServers.length; ++i) {
			if (ns.getPurchasedServerMaxRam() == currentServerRam) {
				await ns.tprint(`You already have the top-of-the-line, daemon ${ns.nFormat(currentServerRam * (1e9), "0.00b")} servers`);
				await ns.sleep(3000);
				await ns.tprint(`Exiting script`);
				await ns.sleep(100);
				ns.exit();
			} else if (bestServerUpgrade <= currentServerRam) {
				await ns.tprint(`Your ${ns.getPurchasedServerLimit()} ${ns.nFormat(currentServerRam * (1e9), "0.00b")} servers are already the best you can afford`);
				await ns.sleep(3000);
				await ns.tprint(`You need ${ns.nFormat(ns.getPurchasedServerCost((currentServerRam) * 2) * (ns.getPurchasedServerLimit()), "$0.000a")} to be able to upgrade your servers`);
				await ns.sleep(3000);
				await ns.tprint(`Exiting script`);
				await ns.sleep(100);
				ns.exit();
			} else {
				await ns.killall(myServers[i]);
				await ns.sleep(100);
				await ns.deleteServer(myServers[i]);
			}
		}
		await ns.tprint(`You can afford ${ns.getPurchasedServerLimit()} new ${ns.nFormat(bestServerUpgrade * (1e9), "0.00b")} servers`);
		await ns.sleep(3000);
		await ns.tprint(`All ${ns.getPurchasedServerLimit()} old ${myServers[0]}-${ns.nFormat(currentServerRam * (1e9), "0.00b")} servers deleted`);
		await ns.sleep(3000);
		await ns.tprint(`Buying ${ns.getPurchasedServerLimit()} new ${ns.nFormat(bestServerUpgrade * (1e9), "0.00b")} servers`);
		await ns.sleep(1000);
		//Buying Upgraded Servers and sending basic script to them
		var i = 0;
		let needRam = ns.getScriptRam("expFarm.ns");

		const MIN_THREADS = 1;
		let threads = Math.max(MIN_THREADS, Math.floor(bestServerUpgrade / needRam));

		while (i < ns.getPurchasedServerLimit()) {
			if (ns.getServerMoneyAvailable("home") > ns.getPurchasedServerCost(bestServerUpgrade)) {
				var hostname = ns.purchaseServer("daemon-" + i, bestServerUpgrade);
				//await ns.scp("Remote/grow-target.js", hostname);
				//await ns.sleep(100)
				//await ns.scp("Remote/hack-target.js", hostname);
				//await ns.sleep(100);
				//await ns.scp("Remote/weaken-target.js", hostname);
				//await ns.sleep(100);
				//await ns.scp("helper.js", hostname);
				//await ns.exec("expFarm.ns", hostname, threads);
			}
			++i
		}
		await ns.tprint(`Scripts sent to all ${ns.getPurchasedServerLimit()} new ${hostname}-${ns.nFormat(bestServerUpgrade * (1e9), "0.00b")} servers`);
		await ns.sleep(3000);
		await ns.tprint(`Script complete`);
		await ns.sleep(100);
		await ns.exit();
	}
}
