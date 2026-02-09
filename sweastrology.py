from swisseph import *

# alias names expected by Morinus
swe_set_ephe_path = set_ephe_path
swe_set_jpl_file = set_jpl_file
swe_close = close
swe_julday = julday
swe_revjul = revjul
swe_deltat = deltat
def swe_calc(jd, ipl, iflag):
	ret = calc(jd, ipl, iflag)
	if isinstance(ret, tuple) and len(ret) == 2:
		a, b = ret
		if isinstance(a, (tuple, list)) and not isinstance(b, (tuple, list)):
			data, res = a, b
		else:
			res, data = a, b
		return res, data, ''
	return ret

def swe_calc_ut(jd_ut, ipl, iflag):
	ret = calc_ut(jd_ut, ipl, iflag)
	if isinstance(ret, tuple) and len(ret) == 2:
		a, b = ret
		if isinstance(a, (tuple, list)) and not isinstance(b, (tuple, list)):
			data, res = a, b
		else:
			res, data = a, b
		return res, data, ''
	return ret
def swe_fixstar(star, jd, iflag):
	ret = fixstar(star, jd, iflag)
	if isinstance(ret, tuple) and len(ret) == 3:
		a, b, c = ret
		if isinstance(a, (tuple, list)) and not isinstance(c, (tuple, list)):
			data, name, res = a, b, c
		else:
			res, name, data = a, b, c
		return res, name, data, ''
	return ret

def swe_fixstar_ut(star, jd_ut, iflag):
	ret = fixstar_ut(star, jd_ut, iflag)
	if isinstance(ret, tuple) and len(ret) == 3:
		a, b, c = ret
		if isinstance(a, (tuple, list)) and not isinstance(c, (tuple, list)):
			data, name, res = a, b, c
		else:
			res, name, data = a, b, c
		return res, name, data, ''
	return ret

def swe_fixstar_mag(star, iflag):
	ret = fixstar_mag(star, iflag)
	if isinstance(ret, tuple) and len(ret) == 2:
		res, mag = ret
		return res, mag, ''
	return ret
swe_get_planet_name = get_planet_name
swe_set_sid_mode = set_sid_mode
swe_set_topo = set_topo
swe_get_ayanamsa = get_ayanamsa
swe_get_ayanamsa_ut = get_ayanamsa_ut
swe_get_ayanamsa_name = get_ayanamsa_name
swe_utc_to_jd = utc_to_jd
swe_jdet_to_utc = jdet_to_utc
swe_jdut1_to_utc = jdut1_to_utc
swe_houses = houses
def swe_houses_ex(tjd_ut, iflag, geolat, geolon, hsys):
	if isinstance(hsys, int):
		hsys = chr(hsys)
	if isinstance(hsys, str):
		hsys_s = hsys
	else:
		try:
			hsys_s = hsys.decode('ascii')
		except Exception:
			hsys_s = hsys
	try:
		hsys_b = hsys_s.encode('ascii')
	except Exception:
		hsys_b = hsys_s
	try:
		ret = houses_ex(tjd_ut, geolat, geolon, hsys_b, iflag)
	except Exception:
		ret = houses(tjd_ut, geolat, geolon, hsys_b)
	if isinstance(ret, tuple) and len(ret) == 2:
		cusps, ascmc = ret
		if isinstance(cusps, (tuple, list)) and (len(cusps) == 12 or (len(cusps) == 13 and cusps[0] != 0)):
			cusps = (0.0,) + tuple(cusps)
		return 0, cusps, ascmc
	return ret
swe_houses_armc = houses_armc
def swe_house_pos(armc, geolat, eps, hsys, lon, lat):
	if isinstance(hsys, int):
		hsys = chr(hsys)
	if isinstance(hsys, str):
		try:
			hsys_b = hsys.encode('ascii')
		except Exception:
			hsys_b = hsys
	else:
		hsys_b = hsys
	try:
		hpos = house_pos(armc, geolat, eps, (lon, lat), hsys_b)
	except Exception:
		hpos = house_pos(armc, geolat, eps, (lon, lat), hsys_b)
	return hpos, ''
swe_gauquelin_sector = gauquelin_sector
swe_sol_eclipse_where = sol_eclipse_where
swe_lun_occult_where = lun_occult_where
swe_sol_eclipse_how = sol_eclipse_how
swe_sol_eclipse_when_loc = sol_eclipse_when_loc
swe_lun_occult_when_loc = lun_occult_when_loc
swe_sol_eclipse_when_glob = sol_eclipse_when_glob
swe_lun_occult_when_glob = lun_occult_when_glob
swe_lun_eclipse_how = lun_eclipse_how
swe_lun_eclipse_when = lun_eclipse_when
swe_pheno = pheno
swe_pheno_ut = pheno_ut
swe_refrac = refrac
swe_refrac_extended = refrac_extended
swe_set_lapse_rate = set_lapse_rate
swe_azalt = azalt
swe_azalt_rev = azalt_rev
def swe_rise_trans(jd_ut, body, starname, iflag, rsmi, lon, lat, alt, atpress=0.0, attemp=0.0):
	geopos = (lon, lat, alt)
	try:
		ret = rise_trans(jd_ut, body, rsmi, geopos, atpress, attemp, iflag)
	except TypeError:
		ret = rise_trans(jd_ut, body, rsmi, lon, lat, alt, atpress, attemp, iflag)
	if isinstance(ret, tuple) and len(ret) == 2:
		res, tret = ret
		if isinstance(tret, (tuple, list)):
			tret = tret[0]
		return res, tret, ''
	return ret
swe_nod_aps = nod_aps
swe_nod_aps_ut = nod_aps_ut
swe_time_equ = time_equ
swe_sidtime0 = sidtime0
swe_sidtime = sidtime
def swe_cotrans(lon, lat=None, dist=None, eps=None):
	if lat is None and dist is None and eps is None:
		return cotrans(lon)
	if eps is None:
		return cotrans((lon, lat, dist), 0.0)
	return cotrans((lon, lat, dist), eps)
swe_cotrans_sp = cotrans_sp
swe_version = version
