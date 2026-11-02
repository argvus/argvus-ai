-- Optional package module. The host provides sparse user overrides.
return function(bind, mod)
	bind(
		"app.ai",
		mod .. " + A",
		hl.dsp.exec_cmd(
			"sh -c 'command -v argvus-ai >/dev/null 2>&1 && exec argvus-ai menu'"
		)
	)
end
