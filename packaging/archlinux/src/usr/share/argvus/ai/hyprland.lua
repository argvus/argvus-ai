-- Optional package module. The host provides sparse user overrides.
return function(bind, mod)
	hl.window_rule({
		match = { class = "argvus-ai" },
		float = true,
		size = "1399 920",
		center = true,
	})
	bind(
		"app.ai",
		mod .. " + A",
		hl.dsp.exec_cmd(
			"sh -c 'command -v argvus-ai >/dev/null 2>&1 && exec argvus-ai menu'"
		)
	)
end
