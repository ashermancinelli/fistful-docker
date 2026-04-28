mkdir -p "${STEAMAPPDIR}" || true 

bash "${STEAMCMDDIR}/steamcmd.sh" \
  +force_install_dir "${STEAMAPPDIR}" \
  +login anonymous \
  +app_update "${STEAMAPPID}" \
  +quit

cd ${STEAMAPPDIR}

bash "${STEAMAPPDIR}/srcds_run" -game "${STEAMAPP}" -console -autoupdate \
			-steam_dir "${STEAMCMDDIR}" \
			-steamcmd_script "${HOMEDIR}/${STEAMAPP}_update.txt" \
			-usercon \
			-port "${SRCDS_PORT}" \
			+map "fof_fistful" \
			+sv_setsteamaccount "${SRCDS_TOKEN}"
